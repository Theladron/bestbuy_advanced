from abc import ABC, abstractmethod
class Promotion(ABC):

    def __init__(self, name):
        self.name = name

    def apply_promotion(self, product, quantity):
        raise NotImplementedError("Only children have promotions")



class SecondHalfPrice(Promotion):

    def apply_promotion(self, product, quantity):
        full_price_quantity = quantity // 2
        half_price_quantity = quantity - full_price_quantity
        return full_price_quantity + half_price_quantity * 0.5


class ThirdOneFree(Promotion):

    def apply_promotion(self, product, quantity):
        free_item_quantity = quantity // 3
        return quantity - free_item_quantity


class PercentDiscount(Promotion):

    def __init__(self, name, percent):
        super().__init__(name)
        self.discount = (100 - percent) / 100


    def apply_promotion(self, product, quantity):
        return quantity * self.discount