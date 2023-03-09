print('hello')

import multiprocessing as mp

def increment(counter):
    counter.value += 1


# counter = mp.Value('i', 1)
if __name__ == '__main__':
    counter = mp.Value('i', 1)

    for i in range(10):
        process = mp.Process(target=increment, args=(counter,))
        process.start()
        process.join()

    print(counter.value)