from sklearn.preprocessing import StandardScaler, LabelEncoder
import pandas as pd

# Standardize features (e.g., scaling numerical values)
def standardize_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Standardizes the numerical features of the dataset to have zero mean and unit variance.

    Args:
    - df (pd.DataFrame): The dataset.

    Returns:
    - pd.DataFrame: The dataset with standardized features.
    """
    scaler = StandardScaler()
    numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
    df[numeric_columns] = scaler.fit_transform(df[numeric_columns])
    
    return df

# Label Encoding for categorical variables
def encode_labels(df: pd.DataFrame, target_column: str) -> pd.DataFrame:
    """
    Encodes categorical variables into numerical labels.

    Args:
    - df (pd.DataFrame): The dataset.
    - target_column (str): The column to encode.

    Returns:
    - pd.DataFrame: The dataset with encoded labels for the target column.
    """
    label_encoder = LabelEncoder()
    df[target_column] = label_encoder.fit_transform(df[target_column])
    
    return df