import os
import pandas as pd

# Check if a file exists
def file_exists(file_path: str) -> bool:
    """
    Checks if a file exists at the given path.

    Args:
    - file_path (str): Path to the file.

    Returns:
    - bool: True if file exists, False otherwise.
    """
    return os.path.isfile(file_path)

# Save DataFrame to CSV
def save_to_csv(df: pd.DataFrame, file_path: str) -> None:
    """
    Saves a DataFrame to a CSV file.

    Args:
    - df (pd.DataFrame): The DataFrame to save.
    - file_path (str): The path to save the file.
    """
    df.to_csv(file_path, index=False)

# Display basic info about the dataset (e.g., shape, column names)
def dataset_info(df: pd.DataFrame) -> None:
    """
    Displays basic information about the dataset.

    Args:
    - df (pd.DataFrame): The dataset.
    """
    print(f"Shape of dataset: {df.shape}")
    print(f"Columns: {df.columns}")
    print(f"First few rows:\n{df.head()}")