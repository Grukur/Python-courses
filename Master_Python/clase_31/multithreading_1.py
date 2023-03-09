# import threading
# import time
import multiprocessing as mp

# def name_and_time(name):
#     print(f'Hello {name}, current time is {time.time()}')
#     print('sleeping for 2 seconds....')
#     time.sleep(2)
#     print('After sleeping.... exiting function')
#
#
# if __name__ == '__main__':
#     thread_list = list()
#
#     for i in range(10):
#         thread = threading.Thread(target=name_and_time, args=('Darold',))
#         thread_list.append(thread)
#
#     for x in thread_list:
#         x.start()
#
#     for x in thread_list:
#         x.join()
#
#     print('Other instruction of the main module....')
#     print('End of the script')

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
