DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS swipes;

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    skills TEXT NOT NULL
);

CREATE TABLE swipes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    liker_id INTEGER NOT NULL,
    liked_id INTEGER NOT NULL,
    FOREIGN KEY (liker_id) REFERENCES users (id),
    FOREIGN KEY (liked_id) REFERENCES users (id)
);

-- Insert the demo users 'Priya' and 'Rohan'
INSERT INTO users (name, skills) VALUES ('priya', 'Project Leader, React');
INSERT INTO users (name, skills) VALUES ('rohan', 'React Dev, Node.js');