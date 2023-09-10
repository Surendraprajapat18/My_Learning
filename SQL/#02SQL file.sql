CREATE DATABASE ORG;
SHOW DATABASES;
USE ORG;

CREATE TABLE Worker (
    WORKER_ID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    FIRST_NAME CHAR(25),
    LAST_NAME CHAR(25),
    SALARY INT(15),
    JOINING_DATE DATETIME,
    DEPARTMENT CHAR(25)
);

INSERT INTO Worker
    (WORKER_ID, FIRST_NAME, LAST_NAME, SALARY, JOINING_DATE, DEPARTMENT) VALUES
         (001, 'Monika', 'Arora', 100000, '14-02-20 09.00.00', 'HR'),
		 (002, 'Surendra', 'Singh', 200000, '4-04-20 09.00.00', 'Admin'),
		 (003, 'Vishal', 'Ahirvar', 300000, '24-04-20 09.00.00', 'HR'),
	     (004, 'Vivek', 'Ahirvar', 400000, '14-06-20 09.00.00', 'Admin'),
	     (005, 'Mohit', 'Singh', 500000, '5-06-20 09.00.00', 'Admin'),
         (006, 'Vipul', 'Arora', 600000, '14-07-20 09.00.00', 'Account'),
		 (007, 'Satish', 'Singh', 700000, '4-07-20 09.00.00', 'Account'),
		 (008, 'Geetika', 'Ahirvar', 800000, '24-08-20 09.00.00', 'HR');
         
SELECT *FROM Worker;