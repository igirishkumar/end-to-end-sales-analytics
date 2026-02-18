# 🧪 Methodology

This document outlines the step‑by‑step methodology used to build the Sales Analytics project.

---

# 1. Data Acquisition

Raw datasets were exported from DAX Studio and provided as CSV files:

- Sales fact table  
- Product dimension  
- Customer dimension  
- Region dimension  
- Date dimension  

---

# 2. Data Cleaning (Python)

Performed in `data_cleaning.py`:

- Removed blank rows  
- Standardized column names  
- Converted data types  
- Parsed dates  
- Validated numeric fields  
- Exported cleaned dataset to `data/processed/`  

---

# 3. Exploratory Data Analysis (EDA)

Performed in `eda_report.ipynb`:

- Summary statistics  
- Missing value analysis  
- Outlier detection  
- Numeric distributions  
- Correlation matrix  
- Joined analysis (sales + products/customers/regions/dates)  
- Visualizations saved to `eda/eda_visuals/`  

---

# 4. Data Modeling (Power BI)

A **star schema** was created:

- Fact: Sales  
- Dimensions: Product, Customer, Region, Date  
- Relationships: Many‑to‑One, single direction  

The Date table was marked as the official date table.

---

# 5. DAX Measures

Key measures created:

- Total Sales  
- Sales CY / PY  
- Profit / Profit Margin  
- Sales Growth %  
- Profit Growth %  
- Units Sold  

---

# 6. Dashboard Development

Visuals included:

- KPI cards  
- Product performance (CY vs PY)  
- Monthly sales trend  
- Customer ranking  
- City sales distribution  
- Channel profitability  

---

# 7. Documentation & Repository Structuring

- EDA notebook  
- Scripts folder  
- Data dictionary  
- Project overview  
- Methodology  
- README.md  

---

This methodology ensures the project is transparent, reproducible, and professionally structured.
