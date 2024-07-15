# Write your MySQL query statement below
# Find the IDs of the invalid tweets
SELECT tweet_id
# from tweets table
FROM Tweets
# invalid if the number of characters is strictly greater than 15
WHERE length(content) > 15;
