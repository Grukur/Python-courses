
class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)

    def __getitem__(self, item):
        return (self.cars[item])

    def __repr__(self):
        return f'<Garage {self.cars}>' #esto es para dar informacion en el dibuging

    def __str__(self):
        return f'Garage with {len(self)} cars' #esto se usa para informacion al usuario

ford = Garage()
ford.cars.append("fiesta")
ford.cars.append("focus")

print(len(ford))
print(ford[0])
print(ford)


