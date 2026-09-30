-- 1. Average price for each rating
SELECT rating, AVG(price) AS average_price
FROM books
GROUP BY rating;

-- 2. 5 most expensive books rated 4 or 5

SELECT *
FROM books
WHERE rating IN (4, 5)
ORDER BY price DESC
LIMIT 5;


-- 3. Number of out-of-stock books per rating
SELECT rating, COUNT(*) AS out_of_stock
FROM books
WHERE instock = 0
GROUP BY rating;