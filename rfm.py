import sqlite3
import pandas as pd

conn = sqlite3.connect(r"d:\e commerce project\ecommerce.db")

rfm_query = """
WITH last_date AS (
    SELECT MAX(order_purchase_timestamp) AS max_date
    FROM orders
    WHERE order_status = 'delivered'
),
rfm_base AS (
    SELECT
        c.customer_unique_id,
        CAST(
            JULIANDAY((SELECT max_date FROM last_date)) -
            JULIANDAY(MAX(o.order_purchase_timestamp))
        AS INTEGER)                         AS recency_days,
        COUNT(DISTINCT o.order_id)          AS frequency,
        ROUND(SUM(p.payment_value), 2)      AS monetary
    FROM orders o
    JOIN customers c  ON o.customer_id = c.customer_id
    JOIN payments p   ON o.order_id = p.order_id
    WHERE o.order_status = 'delivered'
    GROUP BY c.customer_unique_id
),
rfm_scored AS (
    SELECT *,
        CASE
            WHEN recency_days <= 90  THEN 5
            WHEN recency_days <= 180 THEN 4
            WHEN recency_days <= 270 THEN 3
            WHEN recency_days <= 365 THEN 2
            ELSE 1
        END AS r_score,
        CASE
            WHEN frequency >= 5 THEN 5
            WHEN frequency = 4  THEN 4
            WHEN frequency = 3  THEN 3
            WHEN frequency = 2  THEN 2
            ELSE 1
        END AS f_score,
        CASE
            WHEN monetary >= 1000 THEN 5
            WHEN monetary >= 500  THEN 4
            WHEN monetary >= 300  THEN 3
            WHEN monetary >= 100  THEN 2
            ELSE 1
        END AS m_score
    FROM rfm_base
),
rfm_segments AS (
    SELECT *,
        CASE
            WHEN r_score >= 4 AND f_score >= 4              THEN 'Champion'
            WHEN r_score >= 3 AND f_score >= 3              THEN 'Loyal'
            WHEN r_score >= 4 AND f_score <= 2              THEN 'New Customer'
            WHEN r_score <= 2 AND f_score >= 3              THEN 'At Risk'
            WHEN r_score <= 2 AND monetary >= 500           THEN 'Cannot Lose'
            WHEN r_score = 1  AND f_score = 1               THEN 'Lost'
            ELSE                                                 'Potential'
        END AS segment
    FROM rfm_scored
)
SELECT
    segment,
    COUNT(*)                        AS total_customers,
    ROUND(AVG(recency_days), 0)     AS avg_recency_days,
    ROUND(AVG(frequency), 1)        AS avg_frequency,
    ROUND(AVG(monetary), 2)         AS avg_monetary,
    ROUND(SUM(monetary), 2)         AS total_revenue
FROM rfm_segments
GROUP BY segment
ORDER BY total_revenue DESC
"""

df = pd.read_sql_query(rfm_query, conn)
print("=" * 75)
print("RFM CUSTOMER SEGMENTATION")
print("=" * 75)
print(df.to_string(index=False))
conn.close()