class Store:
    """
    Represents a store.

    Attributes:
        _products (list): The list of products
    """

    def __init__(self, product_list=None):
        """
        Initializes a Store instance
        :param product_list: Product instances as list
        """
        self._products = []
        if product_list:
            for product in product_list:
                self.add_product(product)

    def __add__(self, other):
        """
        Magic method. Combines two Store instances into one by adding them together
        :param other: the second Store instance
        :return: combined Store instance
        """
        combined_products = self.get_all_products() + other.get_all_products()
        return Store(combined_products)

    def add_product(self, product):
        """
        Adds a product to the list
        :param product:  Instance of a Product class
        """
        self._products.append(product)

    def remove_product(self, product):
        """
        Removes a product from the list
        :param product: instance of a Product class
        """
        self._products.remove(product)

    def get_total_quantity(self):
        """
        Sums up the quantities of all products in the store
        :return: total quantity as int
        """
        total_products = 0
        for product in self._products:
            total_products += product.quantity
        return f"Total of {total_products} items in store"

    def __contains__(self, item):
        """
        Magic method. Checks if a Product instance is present in the Store product list
        :param item: the Product instance
        :return: True if Product instance is present in Store instance, else False
        """
        for product in self._products:
            if product.name == item.name:
                return True
        return False

    def get_all_products(self):
        """
        Gets all products in the store
        :return: products in the store as list
        """
        active_products = []
        for product in self._products:
            if product.is_active():
                active_products.append(product)
        return active_products

    @staticmethod
    def order(shopping_list):
        """
        Processes the orders from the customers, handles exceptions
        :param shopping_list: product/quantity tuples as list
        :return: total price as float, else error message
        """
        total_price = 0
        for product, quantity in shopping_list:
            try:
                total_price += product.buy(quantity)
            except ValueError as error:
                return (f"Error while making order: {error}\n"
                        f"Total order price before the error occurred: {round(total_price, 2)}")

        return f"Total order price: {round(total_price, 2)}"
