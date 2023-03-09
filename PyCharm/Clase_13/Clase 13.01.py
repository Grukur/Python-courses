

def countdown(n):
    while n > 0:
        yield n
        n -= 1

def countdown2(n):
    while n > 0:
        yield n
        n -= 5

def countdown3(n):
    while n > 0:
        yield n
        n -= 2


tasks = [countdown(10), countdown2(30), countdown3(80)]

while tasks:
    task = tasks[0]
    tasks.remove(task)
    try:
        x = next(task)
        print(x)
        tasks.append(task)
    except StopIteration:
        print('Task finished')