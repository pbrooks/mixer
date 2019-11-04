from core import NamedObject

class Ingredient(NamedObject):

    _percent = None

    _quantity = None

    @property
    def percent(self):
        return self._percent

    @property
    def quantity(self):
        return self._quantity

    def __init__(self, percent):
        self._percent = percent

    def calculate(self, ratio):
        self._quantity = self.percent * ratio

    def __str__(self):
        return "{0}: {1:.2f} [{2}%]".format(self.name, self.quantity, self.percent)


class Water(Ingredient):
    pass


class Flour(Ingredient):
    pass


class Salt(Ingredient):
    pass


class BreadFlour(Flour):
    pass


class RyeFlour(Flour):
    pass


class RyeStarter(Ingredient):
    pass

