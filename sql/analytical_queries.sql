-- Top Selling Products
SELECT
    p.product_name,
    SUM(f.quantity) AS total_quantity
FROM fact_sales f
JOIN dim_product p
ON f.product_id = p.product_id
GROUP BY p.product_name
ORDER BY total_quantity DESC;

-- Monthly Revenue
SELECT
    d.month,
    SUM(f.total_amount) AS revenue
FROM fact_sales f
JOIN dim_date d
ON f.date_id = d.date_id
GROUP BY d.month;