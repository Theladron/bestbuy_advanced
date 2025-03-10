from abc import ABC, abstractmethod
from decimal import Decimal, ROUND_HALF_UP


class Promotion(ABC):
    """
    Represents Promotions added to the Product instance

    Attributes:
        name (str): name of the promotion
        """

    def __init__(self, name):
        """
        Initializes the Promotion instance with its name
        :param name: promotion name as str
        """
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity):
        """
        Abstract Method. Has to be implemented in the children classes

        Raises:
            NotImplementedError: if tried to call
            """
        raise NotImplementedError("Only children have promotions")


class SecondHalfPrice(Promotion):
    """
    Children of Promotion instance. Halves the price of
    every second bought Product instance by adjusting the quantity of the purchase
    """

    def apply_promotion(self, product, quantity):
        """
        Adjusts the quantity of the purchase of Products by halving the price
        of every second bought item
        :param product: the Product instance
        :param quantity: amount of bought items as int
        :return: updated quantity as int
        """
        full_price_quantity = quantity / 2
        full_price_decimal = Decimal(f"{full_price_quantity}")
        full_price_quantity = int(full_price_decimal.quantize(Decimal("1"), rounding=ROUND_HALF_UP))
        half_price_quantity = quantity - full_price_quantity
        return full_price_quantity + half_price_quantity * 0.5


class ThirdOneFree(Promotion):
    """
    Children of Promotion instance. Makes every third purchased Product instance
    free by adjusting the quantity of the purchase
    """

    def apply_promotion(self, product, quantity):
        """
        Adjusts the quantity of the purchase of Product instances by making every
        third item free
        :param product: the Product instance
        :param quantity: amount of bought items as int
        :return: updated quantity as int
        """
        free_item_quantity = quantity // 3
        return quantity - free_item_quantity


class PercentDiscount(Promotion):
    """
    Children of Promotion instance. Adds a percentage discount to the purchase
    by adjusting the quantity
    """

    def __init__(self, name, percent):
        """
        Calls for initialization in the parent class, creates a discount afterward
        :param name: promotion name as name
        :param percent: percent to be discounted as int
        """
        super().__init__(name)
        self.discount = (100 - percent) / 100

    def apply_promotion(self, product, quantity):
        """
        Adjusts the quantity of the purchase by multiplying it by the discount
        :param product: the Product instance
        :param quantity: amount of bought items as int
        :return: updated quantity as float
        """
        return quantity * self.discount
