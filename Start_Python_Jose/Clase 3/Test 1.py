
""" manejador de peliculas"""
import os
i = "x"
def find_title(filename, search_path):
    result = []
    for root, dir, files in os.walk(search_path):
        if filename in files:
            result.append(os.path.join(root, filename))
            #var = "1"
            return result
        elif filename not in files:
            print("Wrong name, movie does not exist")

while i !="q":
    option = input("""
        a - To add a movie to your library.
        l - To see your movies.
        f - To find a movie.
        q - To quit from the program.
        
        Choose your option from the menu:  
        """)
    if option == "q":
        i ="q"
        print("Program finished, thanks and bye")
    elif option == "a":
        new = input("Please, write the name of the movie you want to add: ")
        path = "E:\Python Trash\Inicios\Peliculas"
        with open(os.path.join(path, new), 'x') as fp:
            pass
    elif option == "l":
        list = os.listdir("E:\Python Trash\Inicios\Peliculas")
        print(list)
    elif option == "f":
        look = input("please write the name of the movie you like to find: ")
        print(find_title(look, "E:\Python Trash\Inicios\Peliculas"))

