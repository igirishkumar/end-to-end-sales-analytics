"""
eda_analysis.py
Runs EDA on cleaned sales data and generates summary outputs.
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path

from utils import load_dataset

PROC_PATH = Path("../data/processed/")
EDA_VIS_PATH = Path("../eda/eda_visuals/")

def run_eda():
    df = load_dataset(PROC_PATH / "sales_cleaned.csv")

    EDA_VIS_PATH.mkdir(parents=True, exist_ok=True)

    # Summary
    print(df.describe().T)

    # Missing values
    print(df.isna().sum())

    # Correlation heatmap
    plt.figure(figsize=(8,6))
    numeric_df = df.select_dtypes(include="number")
    sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm")
    plt.title("Correlation Matrix")
    plt.tight_layout()
    plt.savefig(EDA_VIS_PATH / "correlation_matrix.png")
    plt.close()

    print("✔ EDA completed. Visuals saved to eda_visuals/")

if __name__ == "__main__":
    run_eda()
