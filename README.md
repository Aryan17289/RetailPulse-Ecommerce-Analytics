# 🛒 RetailPulse — Brazilian E-Commerce Analytics

> End-to-end data analysis of 99,000+ real orders from Olist, Brazil's largest online marketplace.  
> Covers revenue trends, product performance, regional breakdown, and RFM-based customer segmentation — built with Python, SQL (SQLite), and Power BI.

---

## 📌 Project Overview

RetailPulse analyzes the **Olist E-Commerce dataset** (2016–2018) to surface actionable business insights across four domains: revenue growth, category performance, geographic distribution, and customer retention.

| Metric | Value |
|---|---|
| Orders Analyzed | 99,441 |
| Total Revenue | R$15.42M |
| Time Period | Oct 2016 – Aug 2018 (22 months) |
| Tables in DB | 9 |
| Customers Segmented | 93,357 |
| Delivery Rate | 97.0% |

---

## 🔍 Key Insights

**1. Revenue grew 25x in 13 months** — from R$46K (Oct 2016) to R$1.15M (Nov 2017), with a clear Black Friday spike.

**2. Bed & Bath is the top category** — R$1.69M revenue across 9,272 orders, followed by Health & Beauty (R$1.62M).

**3. São Paulo dominates** — SP alone generates R$5.77M (37% of total revenue), nearly 3× Rio de Janeiro's R$2.05M.

**4. Retention crisis uncovered via RFM** — 93% of 93,357 customers (38,227 "New" vs. only 33 "Champions") never repurchased. The business is almost entirely acquisition-dependent.

**5. AOV declining** — Average Order Value dropped from R$175 (2016) to ~R$155 (2018), signalling pricing pressure worth investigating.

---

## 🗂️ Project Structure

```
RetailPulse/
│
├── data/                          # Raw Olist CSV datasets (8 files)
│   ├── olist_orders_dataset.csv
│   ├── olist_customers_dataset.csv
│   ├── olist_order_items_dataset.csv
│   ├── olist_order_payments_dataset.csv
│   ├── olist_order_reviews_dataset.csv
│   ├── olist_products_dataset.csv
│   ├── olist_sellers_dataset.csv
│   ├── olist_geolocation_dataset.csv
│   └── product_category_name_translation.csv
│
├── powerbi_data/                  # Processed CSVs exported for Power BI
│   ├── monthly_revenue.csv
│   ├── category_revenue.csv
│   ├── state_revenue.csv
│   ├── aov_by_month.csv
│   └── rfm_segments.csv
│
├── load_data.py                   # Loads all CSVs into SQLite DB
├── analysis.py                    # Core SQL queries (revenue, categories, states, AOV)
├── rfm.py                         # RFM scoring + customer segmentation
├── export.py                      # Exports analysis results to CSV for Power BI
├── build_dashboard.py             # Generates standalone HTML dashboard
├── dashboard.html                 # Interactive HTML dashboard (no dependencies)
│
├── Dashboard.pbix                 # Power BI dashboard file
├── ecommerce.db                   # SQLite database (all 9 tables)
└── README.md
```

---

## 🛠️ Tech Stack

| Layer | Tools |
|---|---|
| Data Storage | SQLite (9-table relational schema) |
| Data Processing | Python, Pandas |
| Analysis | SQL (CTEs, Window Functions, JOINs) |
| Segmentation | RFM Analysis (Recency, Frequency, Monetary) |
| Visualization | Power BI, HTML/JavaScript (standalone dashboard) |
| Dataset Source | [Olist via Kaggle](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) |

---

## 🚀 How to Run

### 1. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/RetailPulse-Ecommerce-Analytics.git
cd RetailPulse-Ecommerce-Analytics
```

### 2. Install dependencies
```bash
pip install pandas
```

### 3. Load data into SQLite
```bash
python load_data.py
```
> This reads all 8 CSVs and creates `ecommerce.db` with 9 tables.

### 4. Run analysis
```bash
python analysis.py    # Monthly revenue, top categories, state breakdown, AOV
python rfm.py         # RFM scoring and customer segmentation
```

### 5. Export for Power BI
```bash
python export.py      # Saves 5 CSVs to /powerbi_data/
```

### 6. View the HTML dashboard
Open `dashboard.html` in any browser — no server or installation needed.

---

## 📊 RFM Segmentation Results

| Segment | Customers | Avg Spend (R$) | Total Revenue (R$) |
|---|---|---|---|
| New Customer | 38,227 | 168 | 6,426,016 |
| Potential | 33,953 | 144 | 4,900,878 |
| Lost | 19,284 | 125 | 2,404,974 |
| **Cannot Lose** | **1,665** | **946** | **1,575,046** |
| Loyal | 126 | 457 | 57,623 |
| At Risk | 69 | 425 | 29,331 |
| Champion | 33 | 867 | 28,595 |

> ⚠️ **Critical Finding:** Only 33 Champions exist among 93,357 customers — a 0.035% retention rate. The "Cannot Lose" segment (1,665 customers averaging R$946 spend) represents the highest-value group at risk of churning.

---

## 📸 Dashboard Preview

> Standalone `dashboard.html` — open directly in any browser.

---

## 📁 Dataset

This project uses the **Brazilian E-Commerce Public Dataset by Olist**, available on Kaggle:  
🔗 https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

The dataset contains 100K+ real orders placed on Olist between 2016 and 2018.

---

## ⭐ If this project helped you, consider giving it a star!
