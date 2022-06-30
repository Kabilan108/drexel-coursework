-- BMES 375 Homework 4
-- Tony K. Okeke (tko35)
-- litecli Students.db

-- EXERCISE 1
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
SELECT * FROM students
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
SELECT * FROM courses
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
SELECT * FROM advisors
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
SELECT * FROM courses_students
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


-- EXERCISE 2:
-- Find all students who took 'ART101'
SELECT s.name, c.quarter
	FROM students s, courses c, courses_students cs
	WHERE c.number = 'ART101' AND cs.course_id = c.id AND s.id=cs.student_id
--  +----------+
--  | name     |
--  +----------+
--  | Anderson |
--  | Jones    |
--  | Chen     |
--  +----------+