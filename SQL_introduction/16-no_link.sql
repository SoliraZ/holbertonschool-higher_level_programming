-- Script that lists all records of the table second_table dislaying the score and the name, ordered by score
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
