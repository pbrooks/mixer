from core import NamedObject
import ingredient

class Formula(ingredient.Ingredient):

    ingredients = []

    _quantity = None

    _ratio = None

    _depth = None

    _max_depth = 0

    @property
    def quantity(self):
        return self._quantity

    @property
    def ratio(self):
        return self._ratio

    def calculate_percent(self):
        if self.has_parent:
            return super().percent
        return sum([x.percent for x in self.ingredients])

    def calculate_ratio(self, quantity, percent):
        return quantity / percent if quantity else 0

    def init_ingredients(self):
        for x in self.ingredients:
            x.set_parent(self, self.ratio)
            if isinstance(x, Formula):
                x.init_ingredients()

    def set_parent(self, parent, ratio):
        total_percent = self.calculate_percent()
        super().set_parent(parent, ratio)
        self._ratio = self._quantity / total_percent
        self._depth = parent._depth + 1 if parent._depth is not None else -1
        self._max_depth = parent._max_depth

    def __init__(self, percent = None, quantity = None, max_depth = None):
        percent = self.calculate_percent() if not percent else percent
        super().__init__(percent)

        self._quantity = quantity
        if max_depth is not None:
            self._max_depth = max_depth
            self._depth = 0

        self._ratio = self.calculate_ratio(quantity, percent)

    def __str__(self):
        if not self._depth:
            self.init_ingredients()

        if self.has_parent and self._depth > self._max_depth:
            return super().__str__()

        indent = "\t" * (self._depth + 1) if self._depth else ""

        output = "Formula {0}: {1:.2f} [{2}%]".format(self.name, self.quantity, self.percent)
        for x in self.ingredients:
            output += "\n{0}{1}".format(indent, str(x))

        return output


class Preferment(Formula):
    pass

class SourdoughPreferment(Preferment):
    ingredients =  [
        ingredient.RyeStarter(80),
        ingredient.RyeFlour(100),
        ingredient.Water(50)
    ]

class SourdoughWhite(Formula):

    ingredients = [
        ingredient.BreadFlour(100),
        SourdoughPreferment(40),
        ingredient.Water(72.3),
        ingredient.Salt(2.53)
    ]

class SourdoughWholemeal(Formula):

    ingredients = [
        ingredient.BreadFlour(100),
        SourdoughPreferment(40),
        ingredient.Water(77),
        ingredient.Salt(2.53),
        ingredient.InstantYeast(2),
    ]
