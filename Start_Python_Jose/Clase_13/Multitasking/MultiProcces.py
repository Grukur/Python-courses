import time
from multiprocessing import Process


def ask_user():
    ask_start = time.time()
    print(f'Hello, {input("Enter your name: ")}')
    print(f'ask_user, {time.time() - ask_start}')


def complex_calculation():
    com_start = time.time()
    print('Started calculation...')
    [x ** 2 for x in range(20000000)]
    print(f'complex_calculation, {time.time() - com_start}')


start = time.time()
ask_user()
complex_calculation()
print(f'Single thread total time: {time.time() - start}')

process = Process(target=complex_calculation)
process.start()

d_start = time.time()

ask_user()

process.join()

print(f'Two process total time: {time.time() - d_start}')
