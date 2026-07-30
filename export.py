import sqlite3
import pandas as pd
import os

import os
BASE = os.path.dirname(os.path.abspath(__file__))
conn = sqlite3.connect(os.path.join(BASE, "ecommerce.db"))
CSV_FOLDER = BASE
OUT = os.path.join(BASE, "powerbi_data")

# 1 — Monthly revenue
q1 = """
SELECT 
    STRFTIME('%Y-%m', o.order_purchase_timestamp) AS month,
    COUNT(DISTINCT o.order_id)                    AS total_orders,
    ROUND(SUM(p.payment_value), 2)                AS revenue
FROM orders o
JOIN payments p ON o.order_id = p.order_id
WHERE o.order_status = 'delivered'
GROUP BY month ORDER BY month
"""

# 2 — Category revenue
q2 = """
SELECT 
    t.product_category_name_english AS category,
    COUNT(DISTINCT o.order_id)      AS total_orders,
    ROUND(SUM(p.payment_value), 2)  AS revenue
FROM orders o
JOIN order_items oi  ON o.order_id = oi.order_id
JOIN products pr     ON oi.product_id = pr.product_id
JOIN translation t   ON pr.product_category_name = t.product_category_name
JOIN payments p      ON o.order_id = p.order_id
WHERE o.order_status = 'delivered'
GROUP BY category ORDER BY revenue DESC
"""

# 3 — State revenue
q3 = """
SELECT 
    c.customer_state                AS state,
    COUNT(DISTINCT o.order_id)      AS total_orders,
    ROUND(SUM(p.payment_value), 2)  AS revenue
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
JOIN payments p  ON o.order_id = p.order_id
WHERE o.order_status = 'delivered'
GROUP BY state ORDER BY revenue DESC
"""

# 4 — AOV by month
q4 = """
SELECT
    STRFTIME('%Y-%m', o.order_purchase_timestamp) AS month,
    ROUND(SUM(p.payment_value) / 
          COUNT(DISTINCT o.order_id), 2)           AS avg_order_value
FROM orders o
JOIN payments p ON o.order_id = p.order_id
WHERE o.order_status = 'delivered'
GROUP BY month ORDER BY month
"""

# 5 — RFM segments
q5 = """
WITH last_date AS (
    SELECT MAX(order_purchase_timestamp) AS max_date
    FROM orders WHERE order_status = 'delivered'
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
    JOIN customers c ON o.customer_id = c.customer_id
    JOIN payments p  ON o.order_id = p.order_id
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
)
SELECT *,
    CASE
        WHEN r_score >= 4 AND f_score >= 4        THEN 'Champion'
        WHEN r_score >= 3 AND f_score >= 3        THEN 'Loyal'
        WHEN r_score >= 4 AND f_score <= 2        THEN 'New Customer'
        WHEN r_score <= 2 AND f_score >= 3        THEN 'At Risk'
        WHEN r_score <= 2 AND monetary >= 500     THEN 'Cannot Lose'
        WHEN r_score = 1  AND f_score = 1         THEN 'Lost'
        ELSE                                           'Potential'
    END AS segment
FROM rfm_scored
"""

# Export all
exports = {
    'monthly_revenue.csv':  q1,
    'category_revenue.csv': q2,
    'state_revenue.csv':    q3,
    'aov_by_month.csv':     q4,
    'rfm_segments.csv':     q5,
}

for filename, query in exports.items():
    df = pd.read_sql_query(query, conn)
    df.to_csv(f"{OUT}\\{filename}", index=False)
    print(f"✓ {filename} exported — {len(df):,} rows")

conn.close()
print(f"\nAll files saved to {OUT}")