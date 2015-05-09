class CLI:

    @staticmethod
    def prepare_database(database, file_name):
        database.connect_database()
        database.create_tables_from_file(file_name)

    @staticmethod
    def print_commands():
        print ('-' * 20)
        print ("CINEMA RESERVATION SYSTEM")
        print ("Please choose a command")
        print ("show_movies")
        print ("show_movie_projections <movie_id> [<date>]")

    @staticmethod
    def command_input(database):

        command = input("command>")

        while command != "exit":
            commands = CLI.command_parser(command)
            CLI.read_command(database, commands)

            command = input("command>")

    @staticmethod
    def command_parser(command):
        commands = command.split()

        return tuple(commands)

    @staticmethod
    def read_command(database, command):

        if command[0] == "show_movies" and len(command) == 1:
            CLI.list_all_movies(database)
        elif "show_movie_projections" in command and len(command) <= 3:
            CLI.list_movies_projections(database, command)

        else:
            print ("Invalid command")

    # @staticmethod
    # def list_all_movies(database):
    #     movies = database.show_all_movies()

    #     print("Movies --- Rating")
    #     for i in range(len(movies)):
    #         print("[{}] - {} {}".format(i + 1, movies[i][0], movies[i][1]))

    @staticmethod
    def list_all_movies(database):
        movies = database.show_all_movies()

        print ("Current movies:")

        for movie in movies:
            print("[{}] - {} {}".format(movie[0], movie[1], movie[2]))

    def list_movies_projections(database, command):
        movie_date = None
        movie_id = command[1]

        if len(command) == 2:
            movies = database.show_movie_projections(movie_id, movie_date)

            if movies is None:
                return

            print ("Projections for movie '{}'". format(movies[0][1]))

            for movie in movies:
                print("[{}] - {} {} ({})" .
                      format(movie[0], movie[3], movie[4], movie[2]))

        elif len(command) == 3:
            movie_date = command[2]
            movies = database.show_movie_projections(movie_id, movie_date)

            if movies is None:
                return

            print ("Projections for movie '{}' on date {}"
                   . format(movies[0][1], movies[0][3]))

            for movie in movies:
                print ("[{}] - {} ({})" .
                       format(movie[0], movie[4], movie[2]))

        else:
            print ("Invalid command")
