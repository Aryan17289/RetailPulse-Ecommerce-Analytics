import sqlite3
import pandas as pd

import os
BASE = os.path.dirname(os.path.abspath(__file__))
conn = sqlite3.connect(os.path.join(BASE, "ecommerce.db"))
CSV_FOLDER = BASE
OUT = os.path.join(BASE, "powerbi_data")

# ── Query 1: Revenue by month ──────────────────────────────────────────
print("=" * 55)
print("INSIGHT 1 — Monthly Revenue Trend")
print("=" * 55)

q1 = """
SELECT 
    STRFTIME('%Y-%m', o.order_purchase_timestamp) AS month,
    COUNT(DISTINCT o.order_id)                    AS total_orders,
    ROUND(SUM(p.payment_value), 2)                AS revenue
FROM orders o
JOIN payments p ON o.order_id = p.order_id
WHERE o.order_status = 'delivered'
GROUP BY month
ORDER BY month
"""
df1 = pd.read_sql_query(q1, conn)
print(df1.to_string(index=False))

# ── Query 2: Top 10 product categories by revenue ─────────────────────
print("\n" + "=" * 55)
print("INSIGHT 2 — Top 10 Categories by Revenue")
print("=" * 55)

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
GROUP BY category
ORDER BY revenue DESC
LIMIT 10
"""
df2 = pd.read_sql_query(q2, conn)
print(df2.to_string(index=False))

# ── Query 3: Revenue by customer state ────────────────────────────────
print("\n" + "=" * 55)
print("INSIGHT 3 — Revenue by State (Top 10)")
print("=" * 55)

q3 = """
SELECT 
    c.customer_state                AS state,
    COUNT(DISTINCT o.order_id)      AS total_orders,
    ROUND(SUM(p.payment_value), 2)  AS revenue
FROM orders o
JOIN customers c    ON o.customer_id = c.customer_id
JOIN payments p     ON o.order_id = p.order_id
WHERE o.order_status = 'delivered'
GROUP BY state
ORDER BY revenue DESC
LIMIT 10
"""
df3 = pd.read_sql_query(q3, conn)
print(df3.to_string(index=False))

# ── Query 4: Average order value by month ─────────────────────────────
print("\n" + "=" * 55)
print("INSIGHT 4 — Average Order Value by Month")
print("=" * 55)

q4 = """
SELECT
    STRFTIME('%Y-%m', o.order_purchase_timestamp) AS month,
    ROUND(SUM(p.payment_value) / 
          COUNT(DISTINCT o.order_id), 2)           AS avg_order_value
FROM orders o
JOIN payments p ON o.order_id = p.order_id
WHERE o.order_status = 'delivered'
GROUP BY month
ORDER BY month
"""
df4 = pd.read_sql_query(q4, conn)
print(df4.to_string(index=False))

conn.close()
print("\n✓ All queries done.")