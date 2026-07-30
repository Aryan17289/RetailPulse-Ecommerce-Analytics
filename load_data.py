import pandas as pd
import sqlite3

# All files are in the same folder as this script
CSV_FOLDER = r"d:\e commerce project"

import os
BASE = os.path.dirname(os.path.abspath(__file__))
conn = sqlite3.connect(os.path.join(BASE, "ecommerce.db"))
CSV_FOLDER = BASE
OUT = os.path.join(BASE, "powerbi_data")

print("Loading files into database...")

files = {
    'orders':       'olist_orders_dataset.csv',
    'order_items':  'olist_order_items_dataset.csv',
    'payments':     'olist_order_payments_dataset.csv',
    'customers':    'olist_customers_dataset.csv',
    'products':     'olist_products_dataset.csv',
    'sellers':      'olist_sellers_dataset.csv',
    'reviews':      'olist_order_reviews_dataset.csv',
    'geolocation':  'olist_geolocation_dataset.csv',
    'translation':  'product_category_name_translation.csv',
}

for table_name, filename in files.items():
    filepath = f"{CSV_FOLDER}\\{filename}"
    df = pd.read_csv(filepath)
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    print(f"✓ {table_name} loaded — {len(df):,} rows")

conn.close()
print("\nDone! ecommerce.db created successfully.")