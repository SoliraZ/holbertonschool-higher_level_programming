-- Script that lists all cities in the database hbtn_0d_usa should display cities.id, cities.name, and states.name and sorted by cities.id
SELECT cities.id, cities.name, states.name FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id;
