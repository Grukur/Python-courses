
"""# We've already defined a movie class like this:
class Movie:
    def __init__(self, new_name, new_director):
        self.name = new_name
        self.director = new_director

    # let's try to add a method `print_info()` here:
    def print_info(self):
        print(f'<<{self.name}>> by {self.director}')

my_movie = Movie("The Matrix", "blakos")
print(my_movie.print_info())
print(my_movie.director)"""

# We have a class called Club, and it is initialized like this (no need to change):
class Club:
    def __init__(self, name):
        self.name = name
        self.players = []

    # define a method that allows us to access the i-th player in the club directly via indexing.
    # for example, if some_club is an object of Club class,
    # we can access the i-th player in some_club like this (you may assume i is always valid):
    # some_club[i]
    def __getitem__(self, i):
        return (self.players[i])

    # define a method that returns a string representation of this object,
    # which can be used to recreate this object.
    # The return value should be in such format (beware of the spacing):
    # Club {club_name}: {list_of_players}
    # the club_name and list_of_players should be replaced by the according value of current object
    def pron(self):
        return(f'Club {self.name} has this players: {self.players}')


    # define a method that returns a readable string representation of this object for the user.
    # The return value should be in such format (beware of the spacing):
    # Club {club_name} with {count_of_players} players
    # the club_name and count_of_players should be replaced by the according value of current object
    def __str__(self):
        return f'Club {self.name} has {len(self.players)} players'

    def login(self):
        raise NotImplementedError('es bromita')

# You only need to finish the methods, we will take care of the object creation and call those methods for you!

my_club = Club("Arsenal")
my_club.players.append("Rolf")
my_club.players.append("Mike")
my_club.players.append("Anne")
print(my_club.players)
print(my_club.players[0])
print(my_club)
print(my_club.pron())
my_club.login()


