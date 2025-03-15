import promotions


class Product:
    """
    Represents a product in a store

    Attributes:
        name (str): The name of the product
        _price (float): The price of the product
        _quantity (int): The available quantity of the product
        _active (bool): The status of the product, indicates whether the product is active
        promotion (list): List of Promotion class instances
    """

    def __init__(self, name, price, quantity):
        """
        Initializes a Product instance, raises exceptions
        :param name: name of the product as str
        :param price: price of the product as float
        :param quantity: quantity of the product as int

        Raises:
            NameError: if name is empty
            TypeError: if price is not int/float, quantity is not int or name is not str
            ValueError: if price or quantity is negative
        """
        if not isinstance(name, str):
            raise TypeError(f"Name has to be a string: {name}")
        if not name:
            raise NameError("Name cannot be empty")
        if not isinstance(price, (float, int)):
            raise TypeError(f"Price has to be a number: {price}")
        if not isinstance(quantity, int):
            raise TypeError(f"Quantity has to be a whole number: {quantity}")
        if price < 0 or quantity < 0:
            raise ValueError("Price/Quantity cannot be negative")
        self.name = name
        self.price = float(price)
        self.promotion = []
        self.activate()
        self.quantity = quantity

    @property
    def quantity(self):
        """
        Getter function. Gets the current quantity of the product
        :return: quantity as int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """
        Setter function. Updates the quantity of the product
        :param quantity: quantity as int

        Raises:
            ValueError: if quantity is negative
        """
        self._quantity = quantity
        if self._quantity == 0:
            self.deactivate()

    @property
    def price(self):
        """
        Getter function. Gets the current price of the product
        :return: price as int
        """
        return self._price

    @price.setter
    def price(self, price):
        """
        Setter function. Updates the price of the product
        :param price: price as int
        Raises:

            ValueError: if price is negative
        """
        self._price = price
        if self._price < 0:
            raise ValueError("Price cannot be negative")

    def __lt__(self, other):
        """
        Magic method. Compares if the price of one Product instance is lower than the other
        :param other: second Product instance
        :return: True if price of first Product instance is lower than the other, else false
        """
        return self.price < other.price

    def __gt__(self, other):
        """
        Magic method. Compares if the price of one Product instance is greater than the other
        :param other: second Product instance
        :return: True if price of first Product instance is greater than the other, else false
        """
        return self.price > other.price

    def is_active(self):
        """
        Gets the current state of the product
        :return: activeness of the product as bool
        """
        return self._active

    def activate(self):
        """Activates the product"""
        self._active = True

    def deactivate(self):
        """Deactivates the product"""
        self._active = False

    def __str__(self):
        """
        Magic method. Shows the name, price quantity and promotions of the product
        :return: name, price, quantity, promotions as str
        """
        if self._active:
            show_product = (f"{self.name}, Price: "
                            f"${self.price}, Quantity: {self.quantity}, Promotion(s): ")
            if self.promotion:
                for promotion in self.promotion:
                    show_product += f"{promotion.name} "
            else:
                show_product += "None"
            return show_product

    def buy(self, quantity):
        """
        Buys a given amount of the product, updates quantity depending on
        active promotions, raises exceptions
        :param quantity: quantity that should be bought as int
        :return: total price of the purchase as float

        Raises:
            ValueError: if product is inactive or quantity exceeds the available product quantity
        """
        if not self.is_active():
            raise ValueError("Product Inactive")
        if self.quantity - quantity < 0:
            raise ValueError("Cannot buy more of the product than available")
        self.quantity -= quantity
        quantity = self.get_promotions(quantity)
        return self.price * quantity

    @property
    def promotion(self):
        """
        Getter function. gets the promotion list
        :return: promotions as list
        """
        return self._promotion

    @promotion.setter
    def promotion(self, promotion):
        """
        Setter function. Sets promotion to an empty list if empty, else appends
        a Promotion instance to the list
        :param promotion: Promotion instance
        """
        if not promotion:
            self._promotion = promotion
        else:
            self._promotion.append(promotion)

    def get_promotions(self, quantity):
        """
        Applies promotions in the logical order depending on active promotions
        :param quantity: quantity of the purchase as int
        :return: Updated quantity after applying promotions as float
        """
        # to make sense logically, we have to apply the discounts in a specific order
        promo = next((promotion for promotion in self.promotion
                      if isinstance(promotion, promotions.ThirdOneFree)), None)
        if promo:
            quantity = promo.apply_promotion(self.name, quantity)

        promo = next((promotion for promotion in self.promotion
                      if isinstance(promotion, promotions.SecondHalfPrice)), None)
        if promo:
            quantity = promo.apply_promotion(self.name, quantity)

        promo = next((promotion for promotion in self.promotion
                      if isinstance(promotion, promotions.PercentDiscount)), None)
        if promo:
            quantity = promo.apply_promotion(self.name, quantity)

        return quantity


class NonStockedProduct(Product):
    """
    Children of Product class instance. Represents a Product instance
    that has unlimited quantity
    """

    def __init__(self, name, price):
        """Calls initialization from parent class, then activates to always stay active"""
        super().__init__(name, price, 0)
        self.activate()

    def __str__(self):
        """
        Shows the name, price, quantity and promotions of the product
        :return: name, price, quantity and promotions as str
        """
        show_product = (f"{self.name}, Price: "
                        f"${self.price}, Quantity: Unlimited, Promotion(s): ")
        if self.promotion:
            for promotion in self.promotion:
                show_product += f"{promotion.name} "
        else:
            show_product += "None"
        return show_product

    def buy(self, quantity):
        """
        gets amount the order was bought for by multiplying price with quantity
        :param quantity: amount of items bought as int
        :return: overall price as float
        """
        quantity = self.get_promotions(quantity)
        return self.price * quantity


class LimitedProduct(Product):
    """
    Children of Product class instance. Represents a Product instance
    that can only be bought in quantities of one

    Additional Attributes:
        maximum (int): maximum number of items that can be bought at a time
    """

    def __init__(self, name, price, quantity, maximum):
        """Calls initialization from parent class, then adds a maximum"""
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def __str__(self):
        """
        Shows the name, price, quantity, maximum and promotion of the product
        :return: name, price, quantity, maximum and promotion as str
        """
        if self._active:
            show_product = (f"{self.name}, Price: ${self.price},"
                            f" Quantity: {self._quantity}, Limited to {self.maximum} "
                            f"per order!, Promotion(s): ")
            if self.promotion:
                for promotion in self.promotion:
                    show_product += f"{promotion.name} "
            else:
                show_product += "None"
            return show_product

    def buy(self, quantity):
        """
        Buys a given amount of the product, updates quantity depending on
        active promotion, raises exceptions
        :param quantity: quantity that should be bought as int
        :return: total price of the purchase as float

        Raises:
            ValueError: if product is inactive, more than maximum or too high quantity is bought
        """
        if not self.is_active():
            raise ValueError("Product Inactive")
        if quantity > self.maximum:
            raise ValueError(f"Only {self.maximum} is allowed for this product!")
        if self.quantity - quantity < 0:
            raise ValueError("Cannot buy more of the product than available")
        self.quantity -= quantity
        quantity = self.get_promotions(quantity)
        return self._price * quantity
