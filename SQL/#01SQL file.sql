CREATE DATABASE temp;

USE temp;

CREATE TABLE student (
id INT PRIMARY KEY, 
name VARCHAR(255)worker
);

INSERT INTO student VALUES(1, 'Surendra');

SELECT * FROM student;

DROP DATABASE IF EXISTS temp;

