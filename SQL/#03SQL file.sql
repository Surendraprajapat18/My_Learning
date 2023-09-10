SELECT LAST_NAME, SALARY FROM Worker;

SELECT now();
SHOW TABLES;
SELECT ucase('sURENdrA');
SELECT * FROM Worker WHERE SALARY BETWEEN 200000 AND 600000;

-- reduce OR statements
-- HR, ADMIN
SELECT * FROM Worker WHERE DEPARTMENT = 'HR' OR DEPARTMENT = 'Admin';

-- better way: IN
SELECT * FROM Worker WHERE DEPARTMENT IN('HR', 'Admin');

-- NOT
SELECT * FROM Worker WHERE DEPARTMENT NOT IN('Admin');

-- WILDCARD
 SELECT * FROM Worker WHERE FIRST_NAME LIKE '%o%';

-- sorting using ORDER by
 SELECT * FROM Worker ORDER BY SALARY DESC;
 
 -- DISTINCT
 SELECT DISTINCT department FROM Worker;
 
-- GROUP BY
SELECT department, COUNT(department) FROM Worker GROUP BY department;

-- AVG
SELECT department, AVG(salary) FROM Worker GROUP BY department;

-- MIN
SELECT department, MAX(salary) FROM Worker GROUP BY department;

-- Having 
SELECT Confirmed FROM covid_data GROUP BY Confirmed HAVING Confirmed > 1000;

-- ADD new column
ALTER TABLE covid_data ADD Again_Infected INT NOT NULL DEFAULT DEFAULT;

-- Describe Table 
DESC covid_data;

-- DROP COLUMN
ALTER TABLE covid_data DROP COLUMN Again_Infected;

-- MODIFY
ALTER TABLE covid_data MODIFY Again_Infected DOUBLE NULL;