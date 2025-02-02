import numpy as np
import pandas as pd

# Add random noise to numeric columns
def add_noise(df: pd.DataFrame, noise_level: float = 0.01) -> pd.DataFrame:
    """
    Adds random noise to numeric columns of the DataFrame.

    Args:
    - df (pd.DataFrame): The dataset.
    - noise_level (float): The standard deviation of the noise to be added.

    Returns:
    - pd.DataFrame: The augmented dataset.
    """
    df_noisy = df.copy()
    for column in df.select_dtypes(include=np.number).columns:
        noise = np.random.normal(0, noise_level, size=df[column].shape)
        df_noisy[column] += noise
    return df_noisy