"""
utils.py
Helper functions for loading datasets and common operations.
"""

import pandas as pd

def load_dataset(path):
    """Load a CSV file safely."""
    try:
        return pd.read_csv(path)
    except Exception as e:
        print(f"Error loading {path}: {e}")
        return None
