import multiprocessing as mp
import time

#
# def name_and_time(name):
#     print(f'Hello {name}, current time is {time.time()}')
#     print('sleeping for 2 seconds....')
#     time.sleep(2)
#     print('After sleeping.... exiting function')

#  -------------------------------opcion larga-----------------------

# if __name__ == '__main__':
#     process_list = list()
#
#     for i in range(10):
#         process = mp.Process(target=name_and_time, args=('Darold',))
#         process_list.append(process)
#
#     for x in process_list:
#         x.start()
#
#     for x in process_list:
#         x.join()
#
#     print('Other instruction of the main module....')
#     print('End of the script')

#  -------------------------------opcion corta-----------------------

# if __name__ == '__main__':
#     for i in range(10):
#         process = mp.Process(target=name_and_time, args=('Darold',))
#         process.start()
#     process.join()
#
#     print('Other instruction of the main module....')
#     print('End of the script')

