# Write your MySQL query statement below
# Produce name column from Customer table
SELECT name
FROM Customer
# Select the names of the customer that are not referred by the customer with id = 2.
WHERE referee_id != 2 OR referee_id IS NULL;
