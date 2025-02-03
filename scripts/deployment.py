import joblib
from sklearn.externals import joblib
import os

# Save model to disk
def save_model(model, model_name: str) -> None:
    """
    Saves the trained model to a file for deployment.

    Args:
    - model: The trained machine learning model.
    - model_name (str): The name to use for the saved model file.
    """
    model_path = os.path.join('models', f'{model_name}.pkl')
    joblib.dump(model, model_path)
    print(f"Model saved to {model_path}")

# Load model from disk
def load_model(model_name: str):
    """
    Loads a pre-trained model from disk.

    Args:
    - model_name (str): The name of the model file.

    Returns:
    - model: The loaded model.
    """
    model_path = os.path.join('models', f'{model_name}.pkl')
    if os.path.exists(model_path):
        model = joblib.load(model_path)
        print(f"Model loaded from {model_path}")
        return model
    else:
        print(f"Model {model_name} not found.")
        return None