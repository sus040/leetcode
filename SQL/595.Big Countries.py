# Write your MySQL query statement below
# Select name, population, area columns only
SELECT name, population, area
# From world table 
FROM world
# Filter where area is at least 3000000 or population of at least twenty-five million.
WHERE area >= 3000000 or population >= 25000000;