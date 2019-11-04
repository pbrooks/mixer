from core import NamedObject
import ingredient

class Formula(NamedObject):

    ingredients = []

    @property
    def percent(self):
        return sum([x.percent for x in self.ingredients])

    def calculate(self, quantity):
        total_percent = self.percent
        ratio = quantity / total_percent
        for x in self.ingredients:
            x.calculate(ratio)

    def __init__(self, quantity = 0):
        self.quantity = quantity
        self.calculate(quantity)

    def __str__(self):
        output = "Formula {0}: {1}".format(self.name, self.quantity)
        for x in self.ingredients:
            output += "\n\t{0}".format(str(x))

        return output


class Preferment(ingredient.Ingredient, Formula):
    pass


class SourdoughPreferment(Preferment):

    ingredients =  [
        ingredient.RyeStarter(80),
        ingredient.RyeFlour(100),
        ingredient.Water(50)
    ]

class SourdoughLoaf(Formula):

    ingredients = [
        ingredient.BreadFlour(100),
        SourdoughPreferment(40),
        ingredient.Water(72.3),
        ingredient.Salt(2.53)
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
