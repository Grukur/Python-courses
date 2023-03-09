

def magic():
    i = 0
    mage = 7
    while i < 3:
        usr = int(input('pick a number betwen 0 and 10, you have 3 shots: '))
        if usr == mage:
            print(f'Congratulation, {usr} is the magic number!!!')
            break
        else:
            i += 1
            if i < 3:
                print(f'Sorry, {usr} is not the magic number, try again!')
    else:
        print(f'Sorry mate, you dont have moore shots')


magic()
