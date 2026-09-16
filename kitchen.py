class Quantity:
    def __init__(self, amount, unit):
        self.amount = amount
        self.unit = unit

    def times(self, multiplier):
        return Quantity(self.amount * multiplier, self.unit)

    def plus(self, other):
        return Sum(self, other)

    def reduce(self, unit, converter=None):
     if converter is None:
        return self

     return converter.convert(self, unit)

    def __eq__(self, other):
        return (
            self.amount == other.amount
            and self.unit == other.unit
        )

    def __repr__(self):
        return f"Quantity({self.amount}, {self.unit!r})"


class Sum:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def reduce(self, unit, converter=None):
        left = self.left.reduce(unit, converter)
        right = self.right.reduce(unit, converter)

        return Quantity(left.amount + right.amount, unit)
    
    def times(self, multiplier):
     return Sum(
        self.left.times(multiplier),
        self.right.times(multiplier)
    )


class Converter:
    def __init__(self):
        self.rates = {
            ("oz", "g"): 28.35,
            ("g", "oz"): 1 / 28.35,
        }

    def convert(self, quantity, unit):
        if quantity.unit == unit:
            return quantity

        rate = self.rates[(quantity.unit, unit)]

        return Quantity(
            quantity.amount * rate,
            unit
        )

    def reduce(self, source, unit):
        return source.reduce(unit, self)