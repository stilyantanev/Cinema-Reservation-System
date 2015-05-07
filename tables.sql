PRAGMA foreign_keys = ON;

DROP DATABASE IF EXISTS Cinema;
CREATE DATABASE Cinema;

DROP TABLE Movies IF EXISTS;
CREATE TABLE Movies(
    id INTEGER PRIMARY KEY,
    name TEXT,
    rating REAL
);

DROP TABLE Projections IF EXISTS;
CREATE TABLE Projections(
    id INTEGER PRIMARY KEY,
    movie_id INTEGER,
    type TEXT,
    date TEXT,
    time TEXT,
    FOREIGN KEY (movie_id) REFERENCES Movies(id)
);

DROP TABLE Reservations IF EXISTS;
CREATE TABLE Reservations(
    id INTEGER PRIMARY KEY,
    username TEXT,
    projection_id INT,
    row INT,
    col INT
    FOREIGN KEY (projection_id) REFERENCES Projections(id)
);

INSERT INTO Movies(name, rating)
VALUES ("The Hunger Games: Catching Fire", 7.9),
       ("Wreck-It Ralph", 7.8),
       ("Her", 8.3),
       ("Hot Pursuit", 4.2),
       ("The D Train", 6.4),
       ("Ruth & Alex", 6.6),
       ("Истинският Сен Лоран", 6.4),
       ("I Am Big Bird: The Caroll Spinney Story", 7.4),
       ("Noble", 7.2),
       ("The Seven Five", 7.3);

INSERT INTO Projections(movie_id, type, date, time)
VALUES (1, "3D", "2014-04-01", "15:30"),
       (1, "4DX", "2014-04-02", "12:10"),
       (1, "2D", "2014-04-03", "11:40"),
       (2, "3D", "2014-04-04", "12:00"),
       (2, "2D", "2014-04-05", "19:15"),
       (2, "4DX", "2014-04-03", "18:20"),
       (3, "3D", "2014-04-02", "08:30"),
       (3, "3D", "2014-04-03", "11:30"),
       (4, "2D", "2014-04-02", "12:35"),
       (5, "4DX", "2014-04-08", "10:55"),
       (5, "2D", "2014-04-02", "11:60"),
       (6, "3D", "2014-04-06", "22:40"),
       (6, "3D", "2014-04-05", "21:40"),
       (7, "2D", "2014-04-03", "18:35"),
       (8, "3D", "2014-04-02", "19:40"),
       (9, "4DX", "2014-04-03", "20:20"),
       (10, "3D", "2014-04-02", "19:40"),
       (10, "2D", "2014-04-01", "11:30"),
       (10, "3D", "2014-04-05", "09:20"),
       (10, "4DX", "2014-04-06", "12:10"),
       (10, "4DX", "2014-04-07", "01:35"),
       (10, "2D", "2014-04-08", "15:10");

INSERT INTO Reservations(username, projection_id, row, col)
VALUES ("Pesho", 1, 7, 7),
       ("Marcho", 1, 3, 2),
       ("Slavi", 1, 2, 2),
       ("Kina", 1, 1, 2),
       ("Georgi", 1, 1, 4),
       ("Georgi", 1, 2, 8),
       ("Pesho", 2, 5, 1),
       ("Pesho", 2, 5, 2),
       ("Pesho", 2, 5, 3),
       ("Pesho", 2, 5, 4),
       ("Pesho", 2, 5, 5),
       ("Filip", 2, 6, 2),
       ("Kostadin", 3, 1, 2),
       ("Stilyan", 3, 3, 2),
       ("Maria", 3, 2, 2),
       ("Maria", 3, 8, 8),
       ("Slavi", 5, 1, 1),
       ("Kincho", 5, 2, 2),
       ("Kerka", 6, 3, 3),
       ("Misho", 6, 4, 4),
       ("Hristo", 7, 1, 1),
       ("Ivelin", 7, 9, 9),
       ("Pesho", 7, 10, 10),
       ("Pesho", 8, 2, 2),
       ("Gosho", 9, 2, 2),
       ("Dimitur", 10, 1, 2),
       ("Ivan", 10, 1, 2),
       ("Ivan", 10, 2, 2),
       ("Ivan", 10, 3, 2),
       ("Ivan", 10, 2, 3),
       ("Rado", 10, 2, 5),
       ("Ivo", 10, 1, 3),
       ("Anton", 10, 3, 1),
