from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split
import pandas as pd

# Train a classifier model
def train_model(df: pd.DataFrame, target_column: str, model_type: str = "logistic_regression"):
    """
    Trains a model on the dataset using the specified model type.
    
    Args:
    - df (pd.DataFrame): The dataset.
    - target_column (str): The target column for prediction.
    - model_type (str): Type of model ('logistic_regression' or 'random_forest').

    Returns:
    - model: The trained model.
    """
    X = df.drop(columns=[target_column])
    y = df[target_column]

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    if model_type == "logistic_regression":
        model = LogisticRegression()
    elif model_type == "random_forest":
        model = RandomForestClassifier(n_estimators=100)
    else:
        raise ValueError(f"Unsupported model type: {model_type}")

    # Train the model
    model.fit(X_train, y_train)
    
    # Predict and evaluate model
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)

    print(f"Model Accuracy: {accuracy}")
    print(f"Confusion Matrix:\n{cm}")

    return model

# Model evaluation with custom metrics (e.g., precision, recall, F1-score)
def evaluate_model(model, X_test: pd.DataFrame, y_test: pd.Series):
    """
    Evaluates a trained model using custom metrics.

    Args:
    - model: The trained model.
    - X_test (pd.DataFrame): The test feature data.
    - y_test (pd.Series): The true labels.

    Returns:
    - dict: Dictionary containing custom evaluation metrics.
    """
    from sklearn.metrics import classification_report

    y_pred = model.predict(X_test)
    report = classification_report(y_test, y_pred, output_dict=True)
    
    return report