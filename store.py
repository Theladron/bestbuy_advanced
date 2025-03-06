class Store:
    """
    Represents a store.

    Attributes:
        _products (list): The list of products
    """

    def __init__(self, product_list):
        """
        Initializes a Store instance
        :param product_list: Product instances as list
        """
        self._products = []
        for product in product_list:
            self.add_product(product)


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
            total_products += product.get_quantity()
        return f"Total of {total_products} items in store"


    def get_all_products(self):
        """
        Gets all products in the store
        :return: products in the store as list
        """
        return self._products


    def order(self, shopping_list):
        """
        Processes the orders from the customers, handles exceptions
        :param shopping_list: product/quantity tuples as list
        :return: total price as float, else error message
        """
        total_price = 0
        for product, quantity in shopping_list:
            try:
                total_price += product.buy(quantity)
                if not product.is_active():
                    self.remove_product(product)
            except ValueError as error:
                return (f"Error while making order: {error}.\n"
                        f"Total order price before the error occurred: {total_price}")

        return f"Total order price: {total_price}"
