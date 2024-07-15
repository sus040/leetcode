# Write your MySQL query statement below
# Return product_name, year, and price from each table 
SELECT p.product_name, s.year, s.price
FROM Product p
# Ensure only matching rows are included 
INNER JOIN Sales s
# Match rows based on product_id
ON p.product_id = s.product_id;
