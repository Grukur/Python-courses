
class Fix:
    def __init__(self, amount):
        self.amount = amount

    def __repr__(self):
        return f'<Fixed {self.amount:.2f}>'

    @classmethod
    def from_sum(cls, val1, val2): #al ponerlo classmethod, la puerta que se abre al eredar, queda flexible
        return cls(val1 + val2)


new_number = Fix.from_sum(19.485478, 14.487542)
print(new_number)

class Euro(Fix):
    def __init__(self, amount):
        super().__init__(amount) #se usa para tomar la herencia
        self.symbol = "$"

    def __repr__(self):
        return f'<Euro {self.symbol}{self.amount:.2f}>'

money = Euro.from_sum(16.758, 9.999)
print(money)