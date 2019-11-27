-- Script that lists all cities contained in the database hbtn_0d_usa.
SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states
ON cities.state_id = states.id
-- Results must be sorted in ascending order by cities.id
ORDER BY cities.id ASC;
