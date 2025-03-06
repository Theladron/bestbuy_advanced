class Product:
    """
    Represents a product in a store.

    Attributes:
        name (str): The name of the product
        price (float): The price of the product
        _quantity (int): The available quantity of the product
        _active (bool): The status of the product, indicates whether the product is active
    """


    def __init__(self, name, price, quantity):
        """
        Initializes a Product instance, raises exceptions
        :param name: name of the product as str
        :param price: price of the product as float
        :param quantity: quantity of the product as int

        Raises:
            NameError: if name is empty
            TypeError: if price is not int/float or quantity is not int
            ValueError: if price or quantity is negative
        """
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
        self.activate()
        self.set_quantity(quantity)


    def get_quantity(self):
        """
        Gets the current quantity of the product
        :return: quantity as int
        """
        return self._quantity


    def set_quantity(self, quantity):
        """
        Updates the quantity of the product
        :param quantity: quantity as int
        """
        self._quantity = quantity
        if self._quantity == 0:
            self.deactivate()


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


    def show(self):
        """
        Shows the name, price and quantity of the product
        :return: name, price, quantity as str
        """
        if self._active:
            return f"{self.name}, Price: {self.price}, Quantity: {self._quantity}"


    def buy(self, quantity):
        """
        Buys a given amount of the product, raises exceptions
        :param quantity: quantity that should be bought as int
        :return: total price of the purchase as float

        Raises:
            ValueError: if product is inactive or quantity exceeds the available product quantity
        """
        if not self.is_active():
            raise ValueError("Product Inactive")
        if (self.get_quantity() - quantity) < 0:
            raise ValueError("Quantity larger then what exists")
        self.set_quantity((self.get_quantity() - quantity))
        return self.price * quantity



class NonStockedProduct(Product):


    def __init__(self, name, price):
        super().__init__(name, price, 0)
        self.activate()


    def buy(self, quantity):
        return self.price * quantity


    def show(self):
        """
        Shows the name, price and quantity of the product
        :return: name, price, quantity as str
        """
        if self._active:
            return f"{self.name}, Price: {self.price}, Quantity: Unlimited"


class LimitedProduct(Product):

    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self.maximum = maximum


    def show(self):
        if self._active:
            return f"{self.name}, Price: {self.price}, Limited to 1 per order!"


    def buy(self, quantity):
        if not self.is_active():
            raise ValueError("Product Inactive")
        if quantity != 1:
            raise ValueError("Only 1 is allowed for this product!")
        self.set_quantity((self.get_quantity() - quantity))
        return self.price * quantity
