-- SQL placeholder file
-- Total sales by region
SELECT region, SUM(revenue) AS total_revenue
FROM sales
GROUP BY region;


-- Monthly sales trend
SELECT DATE_TRUNC('month', order_date) AS month, SUM(revenue)
FROM sales
GROUP BY month
ORDER BY month;