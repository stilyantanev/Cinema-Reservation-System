import sqlite3


class ReservationSystem:

    def __init__(self, database):
        self.database = database
        self.connection = None
        self.cursor = None

    def establish_connection(self):
        self.connection = sqlite3.connect(self.database)
        self.cursor = self.connection.cursor()

    def close_connection(self):
        self.connection.close()

    def create_tables_from_file(self, file_name):
        with open(file_name, "r") as f:
            self.cursor.executescript(f.read())

            self.connection.commit()

    def show_all_movies(self):
        show_all_movies_command = """
            SELECT name, rating FROM Movies
            ORDER BY rating DESC"""
        self.cursor.execute(show_all_movies_command)
        all_movies = self.cursor.fetchall()
        return all_movies

    def show_movie_projections(self, movie_id, date=None):
        if date is None:
            show_projections_query = """
            SELECT Movies.name,
                   Projections.type, Projections.date, Projections.time
            FROM Movies JOIN Projections
            ON Movies.id = Projections.movie_id
            """
        self.cursor.execute(show_projections_query)

        # if date is not None:
        #     show_projections_query = """
        #     SELECT Movies.name,
        #            Projections.type, Projections.date, Projections.time
        #     FROM Movies JOIN Projections
        #     ON Movies.id = Projections.movie_id
        #     """

    def count_available_spots(self, proj_id):
        show_spots_command = """
            SELECT projection_id, COUNT(row) AS spots
            FROM Reservations
            WHERE projection_id = proj_id
            GROUP BY projection_id"""
        spots = self.cursor.execute(show_spots_command)
        ReservationSystem.SEATS -= spots

        return ReservationSystem.SEATS

    def check_if_seat_is_free(self, proj_id, row, col):
        get_seat_for_id_command = """
            SELECT row, col
            FROM Reservations
            WHERE projection_id = proj_id"""

        seat = self.cursor.execute(get_seat_for_id_command)

        return seat.fetchall()
