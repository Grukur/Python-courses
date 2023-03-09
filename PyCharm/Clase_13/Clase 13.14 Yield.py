"""def greet():
    friend = yield
    print(f'Hello, {friend}')


g = greet()
g.send(None) # priming the generator - cebando la funcion
g.send('Adam')"""


"""from collections import deque

friends = deque(('Rolf', 'Jose', 'Charlie', 'Jen', 'Anna'))

############# estos generadores se llaman co-routines

def friend_upper():
    while friends:
        friend = friends.popleft().upper()
        greetings = yield # yield funciona como una antena, permite a la funcion recibir info y ademas reemplaza al next
        print(f'{greetings}, {friend}')


def greet(g):
    g.send(None)
    while True:
        greetings = yield # yield funciona como una antena, permite a la funcion recibir info y ademas reemplaza al next
        g.send(greetings)

greeter = greet(friend_upper())
greeter.send(None)
greeter.send('Hello')"""

############### veremos AWAIT keyword

from collections import deque
from types import coroutine

friends = deque(('Rolf', 'Jose', 'Charlie', 'Jen', 'Anna'))

# estos generadores se llaman co-routines

@coroutine
def friend_upper():
    while friends:
        friend = friends.popleft().upper()
        greetings = yield # yield funciona como una antena, permite a la funcion recibir info y ademas reemplaza al next
        print(f'{greetings}, {friend}')


async def greet(g):
    print('Starting ....')
    await g
    print('Ending ....')

greeter = greet(friend_upper())
greeter.send(None)
greeter.send('Hello')