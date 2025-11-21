CREATE DATABASE prototyp;
USE prototyp;

CREATE TABLE test (
    id INT AUTO_INCREMENT PRIMARY KEY,
    message VARCHAR(255)
);

INSERT INTO test (message) VALUES ("Hello from MySQL");
