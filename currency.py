class Currency:

    currencies = {'CHF': 0.930023,  # swiss franc
                  'CAD': 1.264553,  # canadian dollar
                  'GBP': 0.737414,  # british pound
                  'JPY': 111.019919,  # japanese yen
                  'EUR': 0.862361,  # euro
                  'USD': 1.0}  # us dollar

    def __init__(self, value, unit="USD"):
        self.value = value
        self.unit = unit

    def __str__(self):
        return f"{round(self.value,2)} {self.unit}"

    def __repr__(self):
        return f"{round(self.value,2)} {self.unit}"

    def changeTo(self, new_unit):
        """
          An Currency object is transformed from the unit "self.unit" to "new_unit"
        """
        self.value = (
            self.value / Currency.currencies[self.unit] * Currency.currencies[new_unit])
        self.unit = new_unit

    def __add__(self, other):
        """
          Defines the '+' operator.
          If other is a Currency object the currency values 
          are added and the result will be the unit of 
          self. If other is an int or a float, other will
          be treated as a USD value. 
        """
        if type(other) == int or type(other) == float:
            x = (other * Currency.currencies[self.unit])
        else:
            x = (other.value /
                 Currency.currencies[other.unit] * Currency.currencies[self.unit])
        return Currency(x + self.value, self.unit)

    def __iadd__(self, other):
        """
          Similar to __add__
        """
        return Currency.__add__(self, other)

    def __radd__(self, other):
        res = self + other
        if self.unit != "USD":
            res.changeTo("USD")
        return res

    def __sub__(self, other):
        """
          Defines the '+' operator.
          If other is a Currency object the currency values 
          are subtracted and the result will be the unit of 
          self. If other is an int or a float, other will
          be treated as a USD value. 
        """
        if type(other) == int or type(other) == float:
            x = (other * Currency.currencies[self.unit])
        else:
            x = (other.value /
                 Currency.currencies[other.unit] * Currency.currencies[self.unit])
        return Currency(self.value - x, self.unit)

    def __isub__(self, other):
        """

        """
        return Currency.__sub__(self, other)

    def __rsub__(self, other):
        res = other - self.value
        res = Currency(res, self.unit)
        if self.unit != "USD":
            res.changeTo("USD")
        return res


version1 = Currency(23.43, "EUR")
version2 = Currency(19.97, "USD")
print(version1 + version2)
print(version2 + version1)
print(version1 + 3)
print(3 + version1)
print(version1 - 3)
print(30 - version2)
