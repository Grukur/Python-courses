import multiprocessing as mp
import time


# def deposit(balance):
#     for i in range(100):
#         time.sleep(0.01)
#         balance.value += 1
#
#
# def withdraw(balance):
#     for i in range(100):
#         time.sleep(0.01)
#         balance.value -= 1
#
#
# if __name__ == '__main__':
#     balance = mp.Value('i', 500)
#
#     p1 = mp.Process(target=deposit, args=(balance,))
#     p2 = mp.Process(target=withdraw, args=(balance,))
#
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()
#
#     print(balance.value)

#---------------------------- Solucion --------------------------

def deposit(balance, lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        balance.value += 1
        lock.release()


def withdraw(balance, lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        balance.value -= 1
        lock.release()


if __name__ == '__main__':
    balance = mp.Value('i', 500)

    lock = mp.Lock()

    p1 = mp.Process(target=deposit, args=(balance, lock))
    p2 = mp.Process(target=withdraw, args=(balance, lock))

    p1.start()
    p2.start()
    p1.join()
    p2.join()

    print(balance.value)