
list = ["comica", "terror", "romantica", "SCFI", "Test"]

def menu():
i = "x"
while i !="q":
    option = input("""
        a - To add a movie to your library.
        l - To see your movies.
        f - To find a movie.
        q - To quit from the program.
        Choose your option from the menu:  
        """)
    if option == "q":
        i = "q"
        print("Program finished, thanks and bye")

    elif option == "a":
        new = input("Please, write the name of the movie you want to add: ")
        list.append(new)
        print(*list, sep=" * ")
        print("You have added succesfull the new movie")

    elif option == "l":
        print(*list, sep=" * ")
        print("those are all your movies")

    elif option == "f":
        look = input("please write the name of the movie you like to find: ")
        if look in list:
            print("This movie already exist")
        elif look not in list:
            print("Wrong name, movie does not exist")
