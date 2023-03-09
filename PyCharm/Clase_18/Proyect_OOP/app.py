from Clase_18.Proyect_OOP.admin import Admin
from Clase_18.Proyect_OOP.database import Database
from Clase_18.Proyect_OOP.user import User


a = Admin('rolf', '1234', 3)
u = User('jose', 'password')

a.save()

users = [a, u]
for user in users:
    user.save()


print(Database.find(lambda x: x['username'] == 'rolf'))
