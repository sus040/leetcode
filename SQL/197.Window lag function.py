# Write your MySQL query statement below
# Use LAG to compare each day's temperature with the previous day's temperature
SELECT id
FROM (
    SELECT id, 
           temperature, 
           LAG(temperature) OVER (ORDER BY recordDate) AS prev_temperature
    FROM Weather
) sub
# Filter to get only the records where the temperature is higher than the previous day's temperature
WHERE temperature > prev_temperature;
