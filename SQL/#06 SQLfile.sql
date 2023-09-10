-- Sub Query 
use practics2

select * from spotify_data;

select valence, SNO from spotify_data WHERE valence in (select valence from spotify_data where SNO%2=0) order by valence desc;

-- Corelated subquery
-- find 3rd HIGHEST VALENCE
SELECT * FROM spotify_data as s1 
WHERE 3 = (
SELECT COUNT(s1.valence)
FROM spotify_data as s2 
WHERE s2.valence >= s1.valence
);

