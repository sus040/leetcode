# Write your MySQL query statement below
# Show product id 
SELECT product_id 
# from Product tables
FROM Products
# Find ids of products that are both low fat and recyclable
WHERE low_fats = 'Y' AND recyclable = 'Y';