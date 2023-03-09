movies = [{"Movie": "Terror", "Director": "Ale", "Year": "1990"}]

def menu():
    a = "1"
    while a == "1":
        opt = input("""
        a - To add a new movie
        l - To see all the movies in directory
        f - To find a movie you like
        q - To quit        
        
        please select one of the options above: """)

        if opt == "q":
            a = "q"
            print("**** Bye bye ****")
        elif opt == "a":
            add_movie()
        elif opt == "l":
            see_movie(movies)
        elif opt == "f":
            find_movie()


def add_movie():
    new_movie = input("please write the name of the Movie: ")
    new_director = input("please write the name of the Director: ")
    new_year = str(input("please write the year of the Movie: "))
    movies.append({"Movie": new_movie.title(), "Director": new_director.title(), "Year": new_year})


def see_movie(list):
    for movie in list:
        see_details(movie)

def see_details(movie):
    print(f"Movie: {movie['Movie']}")
    print(f"Director: {movie['Director']}")
    print(f"Year: {movie['Year']}","\n")


def find_movie():
    category = input("Please choose from: Movie, Director or Year... ")
    find = input("Please write the name of Movie, Director or the Year of the movie you need: ")

    found_movies = find_by(movies, find, category)
    see_movie(found_movies)

def find_by(items, find, category):
    found = []
    for i in items:
        if category[i] == find:
            found.append(i)
    return found

menu()


