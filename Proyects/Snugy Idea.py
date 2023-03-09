


a = []
def my_function():
    i = int(input('pls give data: '))
    while i > 0:
        if (i % 2) == 0:
            a.append(int(0))
            i = i / 2
        else:
            a.append(int(1))
            i = (i // 2)
    a.reverse()
    print(*a, sep='')

my_function()