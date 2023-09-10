use practics;

select * from sbin;

select open, count(open) from sbin group by open;

use practics2;
select * from covid_data;

ALTER TABLE covid_data ADD Again_Infected INT NOT NULL DEFAULT 0;


