import pandas as pd
import numpy as np

# Load data
def load_data(file_path: str) -> pd.DataFrame:
    """
    Loads the dataset from a CSV file.
    
    Args:
    - file_path (str): Path to the dataset file.

    Returns:
    - pd.DataFrame: Loaded dataset.
    """
    return pd.read_csv(file_path)

# Clean data (e.g., handle missing values, remove duplicates)
def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans the dataset by removing duplicates and handling missing values.

    Args:
    - df (pd.DataFrame): The raw dataset.

    Returns:
    - pd.DataFrame: Cleaned dataset.
    """
    df = df.drop_duplicates()
    df = df.fillna(df.mean())  # Simple approach: fill missing values with column mean
    return df

# Normalize data (e.g., standard scaling)
def normalize_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Normalizes the dataset using standard scaling (z-score).

    Args:
    - df (pd.DataFrame): The cleaned dataset.

    Returns:
    - pd.DataFrame: Normalized dataset.
    """
    return (df - df.mean()) / df.std()

# Main function for preprocessing
def preprocess_data(file_path: str) -> pd.DataFrame:
    """
    Preprocesses the dataset from file by loading, cleaning, and normalizing it.

    Args:
    - file_path (str): Path to the dataset file.

    Returns:
    - pd.DataFrame: The preprocessed dataset.
    """
    df = load_data(file_path)
    df = clean_data(df)
    df = normalize_data(df)
    return df