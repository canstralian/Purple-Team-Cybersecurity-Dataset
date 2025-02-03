import numpy as np
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.utils import resample

# Add polynomial features for data augmentation
def add_polynomial_features(df: pd.DataFrame, degree: int = 2) -> pd.DataFrame:
    """
    Adds polynomial features to the dataset.

    Args:
    - df (pd.DataFrame): The dataset.
    - degree (int): The degree of the polynomial features.

    Returns:
    - pd.DataFrame: The augmented dataset with polynomial features.
    """
    poly = PolynomialFeatures(degree)
    poly_features = poly.fit_transform(df.select_dtypes(include=np.number))
    poly_feature_names = poly.get_feature_names(df.select_dtypes(include=np.number).columns)
    
    # Combine polynomial features with the original dataset
    poly_df = pd.DataFrame(poly_features, columns=poly_feature_names)
    df_augmented = pd.concat([df, poly_df], axis=1)
    
    return df_augmented

# Synthetic oversampling using bootstrap sampling (Resampling)
def oversample_data(df: pd.DataFrame, target_column: str) -> pd.DataFrame:
    """
    Performs oversampling to balance the dataset using bootstrapping.
    
    Args:
    - df (pd.DataFrame): The dataset.
    - target_column (str): The target column to balance.

    Returns:
    - pd.DataFrame: The resampled dataset.
    """
    # Separate majority and minority classes
    majority_class = df[df[target_column] == df[target_column].mode()[0]]
    minority_class = df[df[target_column] != df[target_column].mode()[0]]
    
    # Resample minority class
    minority_resampled = resample(minority_class,
                                  replace=True,  # Allow sampling of the same row more than once
                                  n_samples=majority_class.shape[0],  # Equalize the number of samples
                                  random_state=42)
    
    # Combine majority and minority
    df_resampled = pd.concat([majority_class, minority_resampled])
    
    return df_resampled