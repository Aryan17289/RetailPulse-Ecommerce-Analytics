import sqlite3
import pandas as pd
import os
BASE = os.path.dirname(os.path.abspath(__file__))
conn = sqlite3.connect(os.path.join(BASE, "ecommerce.db"))
CSV_FOLDER = BASE
OUT = os.path.join(BASE, "powerbi_data")

# Test query — orders by status
query = """
SELECT 
    order_status,
    COUNT(*) as total_orders,
    ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER(), 1) as percentage
FROM orders
GROUP BY order_status
ORDER BY total_orders DESC
"""

df = pd.read_sql_query(query, conn)
print(df.to_string(index=False))
conn.close()