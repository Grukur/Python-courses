"""from datetime import datetime, timezone, timedelta

today = datetime.now(timezone.utc)
tomorrow = today + timedelta(hours=-4)

print(today)
print(tomorrow)
print(today.strftime('%d-%m-%Y %H:%M:%S')) #define el formato de la hora y fecha

user_date = input('Please enter yout date in YYYY-mm-dd format: ')
user_date = datetime.strptime(user_date, '%Y-%m-%d')"""

"""import time, timeit

def power(limit):
    return [x**2 for x in range(limit)]

start = time.time()
power(5000000)
end = time.time()

print(end - start)"""

"""def messure_time(func):
    start = time.time()
    func()
    end = time.time()
    print(end - start)

def power(limit):
    return [x**2 for x in range(limit)]

messure_time(lambda: power(500000))

print(timeit.timeit("[x**2 for x in range(10)]")) # rapido, pero de un uso
print(timeit.timeit("list(map(lambda x: x**2, range(10)))")) # lento, pero permite utilizar los datos
# programa para analizar tiempo, profiler"""

import re #este modulo es para utilizar regular expresions, sirve para hacer busquedas (data analisys)

"""email = 'jose@hotmail.com'
expression = '[a-z]+'
expression2 = '[a-z\.]+'

match1 = re.findall(expression, email) # este comando buscara expression dentro de email
match2 = re.findall(expression2, email)

print(match1)

name = match1[0]
domain = f'{match1[1]}.{match1[2]}'
domain2 = match2[1]

print(name)
print(domain, '\n')

print(name)
print(domain2, '\n')"""


"""price = 'Price: $1,189.5045'
expression3 = 'Price: \$([0-9,]*\.[0-9]*)'

match3 = re.search(expression3, price)
print(match3.group(0)) # imrpime todo
print(match3.group(1)) # imprime solo el contenido del primer parentesis

price_nocoma = match3.group(1).replace(',', '')
price_number = float(price_nocoma)
print(price_number)"""