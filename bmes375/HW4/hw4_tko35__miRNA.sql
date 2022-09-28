-- BMES 375 Homework 4
-- Tony K. Okeke (tko35)
-- litecli miRDB.db

-- EXERCISE 3
-- Initialize table
CREATE TABLE miRDB ( name VARCHAR(255), target VARCHAR(255), score FLOAT )

-- Import data from text file to miRDB table
.import 'miRDB_v6.0_prediction_result.txt' miRDB

-- Show first 10 records in table
SELECT * FROM miRDB LIMIT 10
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
	WHERE target = 'NM_005166'
-- verify with awk 
--   `awk '$2 ~ /NM_005166/ { print }' miRDB_v6.0_prediction_result.txt | lc`
--  +-----------+----------+
--  | target    | COUNT(*) |
--  +-----------+----------+
--  | NM_005166 | 27       |
--  +-----------+----------+

-- How many miRNAs are predicted to target NM_005166 and XM_539064?
SELECT COUNT(*) 
	FROM miRDB 
	WHERE target = 'NM_005166' OR target = 'XM_539064'
-- 	+----------+
-- 	| COUNT(*) |
-- 	+----------+
-- 	| 54       |
-- 	+----------+

-- How many predicted targets (genes) of hsa-let-7a-2-3p have a prediction score
-- of at least 80?
SELECT COUNT(*) 
	FROM miRDB 
	WHERE name = 'hsa-let-7a-2-3p' AND score >= 80
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
	LIMIT 10
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