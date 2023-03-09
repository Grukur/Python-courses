
class Demo:
    def __init__(self, song, author, theme):
        self.song = song
        self.author = author
        self.theme = theme
        self.songs = []

        self.menu()

    def menu(self):
        a = "1"
        while a == "1":
            opt = input(""" Hola, bienvenido a tu biblioteca de musica!!!
                        Que deseas hacer hoy?
                        
                        a - Agregar una cancion nueva
                        b - Buscar tu cancion favorita
                        c - Ver todas tus canciones
                        q - Terminar por hoy
                        
                        : """)
            if opt == "q":
                a = "q"
                print("**** Bye bye ****")
            elif opt == "a":
                self.add_song()
            elif opt == "l":
                see_movie(movies)
            elif opt == "f":
                find_movie()

    def add_song(self):
        self.song = input("Por favor, dime el nombre de la cancion: ")
        self.author = input("Por favor, dime el nombre de la autor: ")
        self.theme = input("Por favor, dime el genero de la cancion: ")
        return self.songs.append({"song": self.song, "author": self.author, "theme": self.theme})
        print("tu cancion ha sido guardada con exito!", self.songs())



my_song = Demo("Limbiskit", "Flower", "Rock")

