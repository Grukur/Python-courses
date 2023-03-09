def dis3d():
    # ask user the coordinates of point A and B

    usera = input('Please enter the coordinates of point A, Example: 10 20 30 ').split()
    userb = input('Please enter the coordinates of point B: ').split()

    # I create a list comprehension where we subtract the coordinates ((a(z) - b(z),
    # a(x) - b(x), a(y) - b(y)) then apply power of 2 and that result is append to the list

    headtail = [(float(x) - float(y)) ** 2 for x, y in zip(usera, userb)]

    # with the values created on our list, we sum the values and apply square root of 2
    # to get the final value = distance betwen the 2 points in a 3d space

    distance = (sum(headtail)) ** (1 / 2)

    print(distance)


dis3d()