import sqlite3


class ReservationSystem:

    SEATS = 100

    def __init__(self, database):
        self.database = database
        self.connection = None
        self.cursor = None

    def connect_database(self):
        self.connection = sqlite3.connection(self.database)
        self.cursor = self.cursor.execute()

    def disconnect_database(self):
        self.connection.close()

    def show_all_movies(self):
        show_all_movies_command = """SELECT name FROM Movies ORDER BY rating"""
        self.cursor.execute(show_all_movies_command)

    def show_movie_projections(self, movie_id):
        projections = """
            SELECT movie_id, type, date, time
            FROM movies
            ORDER BY date"""
        self.cursor.execute(projections)

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


