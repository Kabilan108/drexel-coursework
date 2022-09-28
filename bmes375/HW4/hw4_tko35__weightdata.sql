-- BMES 375 Homework 4
-- Tony K. Okeke (tko35)
-- litecli weightdata.sqlite

-- EXERCISE 4
-- Write and execute SQL to get all the data for patients that don't exercise
-- (these patients have timcardio AND timeresist of zero). Show 10 such patients.
SELECT * 
	FROM patient 
	WHERE timecardio = 0 AND timeresist = 0
	LIMIT 10
--  +----+------+--------+---------+------------+-----------+-----------+------------+------------+--------+-----------+---------------+
--  | id | age  | gender | height  | initweight | calintake | jobstatus | timecardio | timeresist | sleep  | steps     | deltaweight   |
--  +----+------+--------+---------+------------+-----------+-----------+------------+------------+--------+-----------+---------------+
--  | 7  | 21.0 | Female | 60.6551 | 153.3522   | 1500.0    | Active    | 0.0        | 0.0        | 6.7495 | 4282.7065 | 3.9967502931  |
--  | 16 | 39.0 | Female | 57.7803 | 133.4423   | 1500.0    | Active    | 0.0        | 0.0        | 7.0986 | 4462.3782 | 10.0285248839 |
--  | 18 | 24.0 | Male   | 69.1721 | 177.2989   | 1500.0    | Active    | 0.0        | 0.0        | 7.4845 | 3446.0754 | -2.5925579337 |
--  | 19 | 41.0 | Male   | 77.9292 | 174.8174   | 1500.0    | Active    | 0.0        | 0.0        | 8.9922 | 4334.9493 | 0.9816860002  |
--  | 28 | 41.0 | Male   | 72.4046 | 196.5634   | 1500.0    | Active    | 0.0        | 0.0        | 9.125  | 3697.5202 | -0.47208183   |
--  | 33 | 47.0 | Female | 66.2543 | 161.1063   | 2079.0394 | Inactive  | 0.0        | 0.0        | 6.1339 | 2847.4379 | 19.0256316026 |
--  | 38 | 36.0 | Male   | 71.0037 | 188.0001   | 1500.0    | Active    | 0.0        | 0.0        | 6.8328 | 4269.779  | 1.0448738713  |
--  | 41 | 43.0 | Female | 60.893  | 120.0183   | 1500.0    | Active    | 0.0        | 0.0        | 7.7737 | 3525.473  | 3.1414766201  |
--  | 43 | 23.0 | Female | 56.2075 | 147.1721   | 1619.0387 | Inactive  | 0.0        | 0.0        | 8.8673 | 2215.8777 | 0.8035095135  |
--  | 50 | 22.0 | Female | 66.9509 | 132.739    | 1500.0    | Active    | 0.0        | 0.0        | 5.8651 | 3446.2415 | 6.6848571278  |
--  +----+------+--------+---------+------------+-----------+-----------+------------+------------+--------+-----------+---------------+

-- Write and execute SQL to count how many patients that don't exercise.
SELECT COUNT(*)
	FROM patient 
	WHERE timecardio = 0 AND timeresist = 0
--  +----------+
--  | COUNT(*) |
--  +----------+
--  | 48       |
--  +----------+

-- Write and execute SQL to count how many patients that are male based on gender
SELECT COUNT(*)
	FROM patient
	WHERE gender = 'MALE'
--  +----------+
--  | COUNT(*) |
--  +----------+
--  | 122      |
--  +----------+

-- Write and execute SQL to count how many patients are active based on jobstatus
SELECT COUNT(*)
	FROM patient
	WHERE jobstatus = 'Active'
--  +----------+
--  | COUNT(*) |
--  +----------+
--  | 129      |
--  +----------+