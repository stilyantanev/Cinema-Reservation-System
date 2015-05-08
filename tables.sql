CREATE TABLE IF NOT EXISTS Movies(
    id INTEGER PRIMARY KEY,
    name TEXT,
    rating DOUBLE
);

CREATE TABLE IF NOT EXISTS Projections(
    id INTEGER PRIMARY KEY,
    movie_id INT,
    type TEXT,
    date DATE,
    time TIME,
    FOREIGN KEY (movie_id) REFERENCES Movies(id)
);

CREATE TABLE IF NOT EXISTS Reservations(
    id INTEGER PRIMARY KEY,
    username TEXT,
    projection_id INT,
    row INT,
    col INT,
    FOREIGN KEY (projection_id) REFERENCES Projections(id)
);
