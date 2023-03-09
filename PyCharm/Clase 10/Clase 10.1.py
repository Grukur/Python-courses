
"""accounts = {
    'cheking': 1950.00,
    'savings': 3695.50
    }

def add_balance(amount, name = 'cheking'):
    accounts[name] += amount
    return accounts[name]

add_balance(500)
print(accounts['cheking'], accounts['savings'])"""

"""def create_acc(name, holder, account_holder):
    account_holder.append(holder)

    return {
        'name': name,
        'main_account_holder': holder,
        'account_holders': account_holder
    }

a1 = create_acc('checking', 'Rolf', [])
a2 = create_acc('savings', 'Jen', [])

print(a2)
print(a1)"""
"""
accounts = {
    'cheking': 1950.00,
    'savings': 3695.50
    }

def add_balance(amount, name = 'cheking'):
    accounts[name] += amount
    return accounts[name]

trasactions = [
    (-180.67, 'checking')
    (-220.00, 'checking')
    (220.67, 'savings')
    (-15.67, 'checking')
    (-23.97, 'checking')
    (-13.00, 'checking')
    (1570.67, 'checking')
    (680.67, 'savings')
]

for t in trasactions:
    add_balance(*t) # el * es para unpack los datos de t in transactions en la funcion add_balance, nos ahorramos especificar t[0], t[1], etc"""

# unpacking

"""class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

users_l = [
    {'username': 'rolf', 'password': '123'},
    {'username': 'dad', 'password': '147'}
        ]"""

"""users = [User.from_dict(x) for x in users_l] # modo de unpack en clase 9
for i in users:
    print(i)"""

"""users = [User(**data) for data in users_l] # modo de unpack mas eficiente
print(users)     """                          # (** en la variable que itinara = **data (se usa 2 * por que retrae key and value
