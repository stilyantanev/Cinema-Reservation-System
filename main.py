from reservation_system import ReservationSystem


def main():
    db = ReservationSystem("cinema.db")
    db.establish_connection()
    db.create_tables_from_file("tables.sql")
    # db.create_tables_from_file("example.sql")

    db.show_movies()
if __name__ == '__main__':
    main()
