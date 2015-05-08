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
        print ("show_movie_projections")

    @staticmethod
    def command_input(database):

        command = input("command>")

        while command != "exit":
            commands = CLI.command_parser(command)
            CLI.command_choice(database, *commands)

            command = input("command>")

        @staticmethod
    def command_parser(command):
        commands = command.split()

        return tuple(commands)

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

        print("Movies --- Rating")
        for i in range(len(all_movies)):
            print("[{}] - {} {}".format( i + 1, all_movies[i][0], all_movies[i][1]))

    def list_movies_projections(database):
        movie_id = input("movie_id>")
