import os
import logging
import pandas as pd
from sklearn.model_selection import train_test_split

# Setup logging for debugging and tracking
def setup_logging(log_file: str = 'data_pipeline.log'):
    """
    Sets up logging for the pipeline to track progress and debug.
    
    Args:
    - log_file (str): Path to the log file.
    """
    logging.basicConfig(filename=log_file,
                        level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')
    logging.info("Logging setup complete.")

# Split dataset into training and testing sets
def split_data(df: pd.DataFrame, target_column: str, test_size: float = 0.2):
    """
    Splits the dataset into training and testing sets.

    Args:
    - df (pd.DataFrame): The dataset.
    - target_column (str): The column to predict.
    - test_size (float): The proportion of data to use for testing.

    Returns:
    - tuple: X_train, X_test, y_train, y_test.
    """
    X = df.drop(columns=[target_column])
    y = df[target_column]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)
    
    return X_train, X_test, y_train, y_test

# Save DataFrame to CSV
def save_dataframe_to_csv(df: pd.DataFrame, file_path: str):
    """
    Saves the DataFrame to a CSV file.

    Args:
    - df (pd.DataFrame): The dataset to save.
    - file_path (str): Path where the CSV will be saved.
    """
    df.to_csv(file_path, index=False)
    logging.info(f"Data saved to {file_path}")

# Load DataFrame from CSV
def load_dataframe_from_csv(file_path: str) -> pd.DataFrame:
    """
    Loads a CSV file into a DataFrame.

    Args:
    - file_path (str): Path to the CSV file.

    Returns:
    - pd.DataFrame: Loaded dataset.
    """
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        logging.info(f"Data loaded from {file_path}")
        return df
    else:
        logging.error(f"{file_path} does not exist.")
        return pd.DataFrame()