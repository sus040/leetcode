# Write your MySQL query statement below
# Return unique_id and name columns from Employees table
SELECT u.unique_id, e.name
FROM Employees e
# Use LEFT JOIN to include EmployeeUNI table
LEFT JOIN EmployeeUNI u
# Match rows where id in Employees equals id in EmployeeUNI
ON e.id = u.id;
