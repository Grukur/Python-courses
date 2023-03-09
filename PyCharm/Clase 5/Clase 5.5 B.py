"""class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __repr__(self):
        return f'<Car {self.make} {self.model}>'

class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)

    def add_cars(self, car):
        if not isinstance(car, Car):
            raise ValueError(f'tried to add a {car.__class__.__name__} to the garage, but you can only add ')
        self.cars.append(car)

autos = Garage()
fiesta = Car('Ford', 'Fiesta')
opel = Car('Opel', 'Insignia')

autos.add_cars(opel)

try:
    autos.add_cars("opel") #este intento con try, funciona para atrapar ciertos errores y que el programa siga funcionando, en este caso, atrapara los errores de Type Error
except TypeError:
    print('Your car was not a car')
except ValueError:
    print('This is weird')
finally:
    print(f'Garage now has {len(autos)} cars.')"""




"""if isinstance(fiesta, Car):
    ford.add_cars(fiesta)
else:
    print('Your car is no a car')"""

class User:
    def __init__(self, name, engage):
        self.name = name
        self.engage = engage
        
    def __repr__(self):
        return f'<User {self.name}>'
    
def get_user_score(user):
    try:
        user.score = calculation(user.engage)
    except KeyError:
        print('Incorrect value')
    else:
        if user.score > 500:
            notification(user)

def calculation(metrics):
    return metrics['clicks'] * 5 + metrics['hits'] * 2

def notification(user):
    print(f'notification sen to {user}')
    
my_user = User('Rolf', {'clicks': 61, 'hits': 100})
get_user_score(my_user)
    
