# Configuration file for model parameters and preprocessing settings

class Config:
    # Data Preprocessing Settings
    missing_value_strategy = "mean"  # Options: 'mean', 'median', 'drop'

    # Model Settings
    model_type = "random_forest"  # Options: 'logistic_regression', 'random_forest'
    random_forest_n_estimators = 100

    # Augmentation Settings
    noise_level = 0.01  # For noise augmentation
    polynomial_degree = 2  # For polynomial feature augmentation

    # Data Sampling Settings
    target_column = "target"  # Name of the target column for resampling
    oversample = True  # Whether to apply oversampling

# Example of using the config:
# config = Config()
# print(config.model_type)