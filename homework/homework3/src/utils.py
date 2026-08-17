# src/utils.py
import pandas as pd

def get_summary_stats(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate descriptive statistics for numeric columns in a DataFrame.
    """
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a pandas DataFrame.")
    return df.describe()

def get_category_summary(df: pd.DataFrame, group_col: str = 'category', val_col: str = 'value') -> pd.DataFrame:
    """
    Aggregate numerical values by category.
    """
    if group_col not in df.columns or val_col not in df.columns:
        raise ValueError("Specified columns not found in DataFrame.")
    return df.groupby(group_col)[val_col].agg(['count', 'mean', 'sum', 'std']).reset_index()