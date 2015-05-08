from reservation_system import ReservationSystem
from command_line_interface import CLI


def main():
    db = ReservationSystem("cinema.db")
    db.establish_connection()
    db.create_tables_from_file("tables.sql")
    # db.create_tables_from_file("example.sql")

    CLI.list_all_movies(db)
if __name__ == '__main__':
    main()
