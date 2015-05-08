class CLI:

    @staticmethod
    def print_commands():
        print ('-' * 20)
        print ("CINEMA RESERVATION SYSTEM")
        print ("Please choose a command")
        print ("show_movies")
        print ("show_movie_projections")

    @staticmethod
    def command_input(database):
        command = input("command>")

        while command != "exit":
            CLI.choose_command(database, command)
            command = input("command>")

    @staticmethod
    def read_command(database, command):
        if command == "show_movies":
            CLI.list_all_movies(database)
        elif command == "show_movie_projections":
            CLI.list_all_movies(database)

        else:
            print ("Invalid command")

    @staticmethod
    def list_all_movies(database):
        movies = database.show_movies()

        for movie in movies:
            print ("[{}] - {} ({})". format(movie[0], movie[1], movie[2]))

    def list_movies_projections(database):
        movie_id = input("movie_id>")
