"""
data_cleaning.py
Cleans raw sales data and exports processed version.
"""

import pandas as pd
from pathlib import Path

RAW_PATH = Path("../data/raw/")
PROC_PATH = Path("../data/processed/")

def clean_sales_data():
    df = pd.read_csv(RAW_PATH / "sales_raw.csv")

    df = df.dropna(how="all").reset_index(drop=True)

    df.columns = (
        df.columns.str.strip()
                  .str.lower()
                  .str.replace(" ", "_")
                  .str.replace("-", "_")
    )

    df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
    df["ship_date"] = pd.to_datetime(df["ship_date"], errors="coerce")

    numeric_cols = ["order_quantity", "unit_selling_price", "unit_cost", "sales", "total_cost", "profit"]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    PROC_PATH.mkdir(exist_ok=True)
    df.to_csv(PROC_PATH / "sales_cleaned.csv", index=False)

    print("✔ Sales data cleaned and saved to processed folder.")

if __name__ == "__main__":
    clean_sales_data()
