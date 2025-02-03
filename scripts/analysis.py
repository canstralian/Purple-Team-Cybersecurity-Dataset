import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Plot a heatmap of correlations between features
def plot_correlation_heatmap(df: pd.DataFrame) -> None:
    """
    Plots a heatmap showing the correlations between numeric features in the dataset.
    
    Args:
    - df (pd.DataFrame): The dataset.
    """
    correlation_matrix = df.corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt='.2f', linewidths=0.5)
    plt.title("Correlation Heatmap")
    plt.show()

# Plot feature distribution for each numeric feature
def plot_feature_distributions(df: pd.DataFrame) -> None:
    """
    Plots the distribution of each numeric feature in the dataset.
    
    Args:
    - df (pd.DataFrame): The dataset.
    """
    numeric_columns = df.select_dtypes(include=[np.number]).columns
    df[numeric_columns].hist(figsize=(12, 10), bins=30, edgecolor='black')
    plt.suptitle("Feature Distributions")
    plt.show()

# Feature importance based on a model (Random Forest example)
def plot_feature_importance(model, X_train: pd.DataFrame) -> None:
    """
    Plots the feature importance based on the trained model.
    
    Args:
    - model: The trained model (Random Forest).
    - X_train (pd.DataFrame): The training feature data.
    """
    feature_importances = model.feature_importances_
    feature_names = X_train.columns
    sorted_idx = feature_importances.argsort()

    plt.figure(figsize=(10, 6))
    plt.barh(feature_names[sorted_idx], feature_importances[sorted_idx])
    plt.title("Feature Importance")
    plt.xlabel("Importance")
    plt.show()