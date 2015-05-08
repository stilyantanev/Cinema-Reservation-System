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
            SELECT id, name, rating FROM Movies
            ORDER BY rating DESC"""
        self.cursor.execute(show_all_movies_command)
        all_movies = self.cursor.fetchall()
        return all_movies

    def show_movie_projections(self, input_id, input_date=None):
        check_input_id = """
            SELECT MAX(Projections.movie_id) AS max_id
            FROM Projections"""

        max_id = (self.cursor.execute(check_input_id)).fetchone()[0]

        if int(input_id) > max_id:
            return None

        if input_date is None:
            show_projections_query = """
            SELECT Movies.id, Movies.name,
                   Projections.type, Projections.date, Projections.time
            FROM Movies
            JOIN Projections
            ON Movies.id = Projections.movie_id
            WHERE Movies.id = ?
            ORDER BY Projections.date ASC
            """
            self.cursor.execute(show_projections_query, input_id)
            all_movies = self.cursor.fetchall()

            return all_movies

        if input_date is not None:
            show_projections_query = """
            SELECT Movies.id, Movies.name,
                   Projections.type, Projections.date, Projections.time
            FROM Movies JOIN Projections
            ON Movies.id = Projections.movie_id
            WHERE Projections.movie_id = ? AND Projections.date = ?
            ORDER BY Projections.time ASC
            """
            self.cursor.execute(show_projections_query, (input_id, input_date))
            all_movies = self.cursor.fetchall()

            return all_movies

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
