CREATE TABLE users(
 id INTEGER PRIMARY KEY,
 username VARCHAR(100),
 email VARCHAR(100) UNIQUE,
 password VARCHAR(255),
 role VARCHAR(50)
);

CREATE TABLE trainers(
 id INTEGER PRIMARY KEY,
 name VARCHAR(100),
 specialization VARCHAR(100),
 experience INTEGER
);

CREATE TABLE members(
 id INTEGER PRIMARY KEY,
 name VARCHAR(100),
 age INTEGER,
 phone VARCHAR(20),
 email VARCHAR(100) UNIQUE,
 membership_type VARCHAR(100),
 trainer_id INTEGER
);

CREATE TABLE subscriptions(
 id INTEGER PRIMARY KEY,
 member_id INTEGER,
 start_date DATE,
 end_date DATE,
 amount FLOAT,
 status VARCHAR(20)
);
