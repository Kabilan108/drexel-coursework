-- BMES 375 Homework 4
-- Tony K. Okeke (tko35)



-- EXERCISE 1 (Students.db)
-- #> litecli Students.db
-- Create 'students' table
CREATE TABLE students (
  id INTEGER PRIMARY KEY,
  name VARCHAR(255),
  birth DATE,
  gpa FLOAT,
  grad INTEGER,
  advisor_id INTEGER
);
-- Add data to table
INSERT INTO students(name, birth, gpa, grad, advisor_id)
	VALUES
	  ('Anderson', '1987-10-22', 3.9, 2009, 2),
	  ('Jones', '1990-04-16', 2.4, 2012, 1),
	  ('Hernandez', '1989-08-12', 3.1, 2011, 1),
	  ('Chen', '1990-02-04', 3.2, 2011, 1);
-- Show table
SELECT * FROM students;
--  +----+-----------+------------+-----+------+------------+
--  | id | name      | birth      | gpa | grad | advisor_id |
--  +----+-----------+------------+-----+------+------------+
--  | 1  | Anderson  | 1987-10-22 | 3.9 | 2009 | 2          |
--  | 2  | Jones     | 1990-04-16 | 2.4 | 2012 | 1          |
--  | 3  | Hernandez | 1989-08-12 | 3.1 | 2011 | 1          |
--  | 4  | Chen      | 1990-02-04 | 3.2 | 2011 | 1          |
--  +----+-----------+------------+-----+------+------------+

-- Create 'courses' table
CREATE TABLE courses (
  id INTEGER PRIMARY KEY,
  number VARCHAR(30),
  name VARCHAR(255),
  quarter VARCHAR(30)
);
-- Add data to table
INSERT INTO courses(number, name, quarter)
	VALUES
	  ('CS142', 'Web stuff', 'Winter 2009'),
	  ('ART101', 'Finger painting', 'Fall 2008'),
	  ('ART101', 'Finger painting', 'Winter 2009'),
	  ('PE204', 'Mud wrestling', 'Winter 2009');
-- Show table
SELECT * FROM courses;
--  +----+--------+-----------------+-------------+
--  | id | number | name            | quarter     |
--  +----+--------+-----------------+-------------+
--  | 1  | CS142  | Web stuff       | Winter 2009 |
--  | 2  | ART101 | Finger painting | Fall 2008   |
--  | 3  | ART101 | Finger painting | Winter 2009 |
--  | 4  | PE204  | Mud wrestling   | Winter 2009 |
--  +----+--------+-----------------+-------------+

-- Create 'advisors' table
CREATE TABLE advisors (
  id INTEGER PRIMARY KEY,
  name VARCHAR(255),
  title VARCHAR(30)
);
-- Add data to table
INSERT INTO advisors(name, title)
	VALUES
	  ('Fujimura', 'prof'),
	  ('Bolosky', 'prof');
-- Show table
SELECT * FROM advisors;
--  +----+----------+-------+
--  | id | name     | title |
--  +----+----------+-------+
--  | 1  | Fujimura | prof  |
--  | 2  | Bolosky  | prof  |
--  +----+----------+-------+

-- Create 'courses_students' table
CREATE TABLE courses_students (
  course_id INTEGER,
  student_id INTEGER
);
-- Add data to table
INSERT INTO courses_students(course_id, student_id)
	VALUES
  	(1, 1), (3, 1), (4, 1), (1, 2),
  	(2, 2), (1, 3), (2, 4), (4, 4);
-- Show table
SELECT * FROM courses_students;
--  +-----------+------------+
--  | course_id | student_id |
--  +-----------+------------+
--  | 1         | 1          |
--  | 3         | 1          |
--  | 4         | 1          |
--  | 1         | 2          |
--  | 2         | 2          |
--  | 1         | 3          |
--  | 2         | 4          |
--  | 4         | 4          |
--  +-----------+------------+


-- EXERCISE 2: (Students.db)
-- #> litecli Students.db
-- Find all students who took 'ART101' and the quarter they took it in
SELECT s.name, c.quarter
	FROM students s, courses c, courses_students cs
	WHERE c.number = 'ART101' AND cs.course_id = c.id AND s.id=cs.student_id;
--  +----------+-------------+
--  | name     | quarter     |
--  +----------+-------------+
--  | Anderson | Winter 2009 |
--  | Jones    | Fall 2008   |
--  | Chen     | Fall 2008   |
--  +----------+-------------+


-- EXERCISE 3
-- #> litecli miRNA.db
-- Initialize table
CREATE TABLE miRDB ( name VARCHAR(255), target VARCHAR(255), score FLOAT );

-- Import data from text file to miRDB table
.import 'miRDB_v6.0_prediction_result.txt' miRDB;

-- Show first 10 records in table
SELECT * FROM miRDB LIMIT 10;
--  +--------------+--------------+------------------+
--  | name         | target       | score            |
--  +--------------+--------------+------------------+
--  | cfa-miR-1185 | XM_537211    | 59.3438099752    |
--  | cfa-miR-1185 | XM_536047    | 54.527           |
--  | cfa-miR-1185 | XM_005617022 | 55.1716326075    |
--  | cfa-miR-1185 | XM_014117861 | 57.4409058608    |
--  | cfa-miR-1185 | XM_014107884 | 57.1519          |
--  | cfa-miR-1185 | XM_005626419 | 67.0536          |
--  | cfa-miR-1185 | XM_005618203 | 62.64            |
--  | cfa-miR-1185 | NM_001252367 | 58.9597687709186 |
--  | cfa-miR-1185 | XM_005621885 | 78.529415636     |
--  | cfa-miR-1185 | XM_005622017 | 58.8579982864    |
--  +--------------+--------------+------------------+

-- How many miRNAs are predicted to target NM_005166?
SELECT target, COUNT(*) 
	FROM miRDB 
	WHERE target = 'NM_005166';
--  +-----------+----------+
--  | target    | COUNT(*) |
--  +-----------+----------+
--  | NM_005166 | 27       |
--  +-----------+----------+

-- How many miRNAs are predicted to target NM_005166 and XM_539064?
SELECT COUNT(*) 
	FROM miRDB 
	WHERE target = 'NM_005166' OR target = 'XM_539064';
-- 	+----------+
-- 	| COUNT(*) |
-- 	+----------+
-- 	| 54       |
-- 	+----------+

-- How many predicted targets (genes) of hsa-let-7a-2-3p have a prediction score
-- of at least 80?
SELECT COUNT(*) 
	FROM miRDB 
	WHERE name = 'hsa-let-7a-2-3p' AND score >= 80;
--  +----------+
--  | COUNT(*) |
--  +----------+
--  | 529      |
--  +----------+

-- List the miRNAs and the number of their targets that have a prediction score
-- of at leat 80 and group them by name. Show only top 10 rows of the result.
SELECT name, COUNT(target)
	FROM miRDB
	WHERE score >= 80
	GROUP BY name
	ORDER BY COUNT(target) DESC
	LIMIT 10;
--  +-----------------+---------------+
--  | name            | count(target) |
--  +-----------------+---------------+
--  | mmu-miR-7116-3p | 4616          |
--  | mmu-miR-6951-3p | 4194          |
--  | hsa-miR-3163    | 4080          |
--  | gga-miR-6701-3p | 3913          |
--  | gga-miR-1786    | 3820          |
--  | hsa-miR-5011-5p | 3623          |
--  | hsa-miR-3613-3p | 3565          |
--  | cfa-miR-8881    | 3512          |
--  | hsa-miR-190a-3p | 2980          |
--  | cfa-miR-8843    | 2939          |
--  +-----------------+---------------+



-- EXERCISE 4
-- #> litecli miRNA.db
-- Write and execute SQL to get all the data for patients that don't exercise
-- (these patients have timcardio AND timeresist of zero). Show 10 such patients.
SELECT * 
	FROM patient 
	WHERE timecardio = 0 AND timeresist = 0
	LIMIT 10;
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
	WHERE timecardio = 0 AND timeresist = 0;
--  +----------+
--  | COUNT(*) |
--  +----------+
--  | 48       |
--  +----------+

-- Write and execute SQL to count how many patients that are male based on gender
SELECT COUNT(*)
	FROM patient
	WHERE gender = 'MALE';
--  +----------+
--  | COUNT(*) |
--  +----------+
--  | 122      |
--  +----------+

-- Write and execute SQL to count how many patients are active based on jobstatus
SELECT COUNT(*)
	FROM patient
	WHERE jobstatus = 'Active';
--  +----------+
--  | COUNT(*) |
--  +----------+
--  | 129      |
--  +----------+