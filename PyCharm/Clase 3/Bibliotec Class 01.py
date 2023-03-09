movies = []

class Biblio:
    def __init__(self, new_name, new_author, new_year, new_theme):
        self.name = new_name
        self.author = new_author
        self.year = new_year
        self.theme = new_theme

    def menu(self):
        a = "1"
        while a == "1":
            opt = input("""
            a - To add a new name.
            l - To see all the movies in directory.
            f - To find a movie you like.
            q - To quit.

            please select one of the options above: """)

            if opt == "q":
                a = "q"
                print("**** Bye bye ****")
            elif opt == "a":
                self.add_movie(self)
            elif opt == "l":
                self.see_movie(self)
            """elif opt == "f":
                find_movie()"""

    def add_movie(self):
        new_name = input("please write the Name: ")
        new_author = input("please write the Author: ")
        new_year = str(input("please write the Year: "))
        new_theme = input("Please write the Theme")
        movies.append({"Movie": new_name.title(), "Director": new_author.title(), "Year": new_year, "Theme": new_theme.title()})

    def see_movie(self):
        for movie in movies:
            print(f"Movie: {movie['Movie']}")
            print(f"Director: {movie['Director']}")
            print(f"Year: {movie['Year']}", "\n")


    menu()

biblio_one = Biblio("Terror", "Ale", "1990", "Pelicula")