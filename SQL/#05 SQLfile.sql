use org;
select * from worker;

-- REPLACE 
replace into worker(WORKER_ID, FIRST_NAME, SALARY) values(4, 'Vivek', 10000);

REPLACE INTO worker(WORKER_ID, FIRST_NAME, DEPARTMENT)
	SELECT WORKER_ID, FIRST_NAME, DEPARTMENT
    FROM worker WHERE WORKER_ID = 6;
    
use practics2;
select * from spotify_data;

select * from covid_data;

-- RENAME TABLE NAME
ALTER TABLE spotify_data CHANGE COLUMN MyUnknownColumn SNO VARCHAR(1024);

-- INNER JOIN
select c.SNO, c.Confirmed, c.Deaths, s.SNO, s.name, s.track_number from covid_data as c
INNER JOIN spotify_data as s ON c.SNO=s.track_number;

-- can we use join w/o using use keyword Ans = Yes
select * from spotify_data, covid_data where spotify_data.SNO = covid_data.SNO;

-- SET operation
select * from spotify_data union select* from covid_data;
