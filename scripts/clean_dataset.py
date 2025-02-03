import pandas as pd
import os

DATA_DIR = "data/"
OUTPUT_DIR = "processed_data/"

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

def clean_dataset(file_path):
    df = pd.read_csv(file_path)

    # Remove duplicates
    df = df.drop_duplicates()

    # Handle missing values (fill with 0 or drop)
    df = df.fillna(0)

    # Normalize specific columns (example: log timestamps)
    if 'timestamp' in df.columns:
        df['timestamp'] = pd.to_datetime(df['timestamp'])

    # Save cleaned dataset
    output_path = os.path.join(OUTPUT_DIR, os.path.basename(file_path))
    df.to_csv(output_path, index=False)
    print(f"Processed: {file_path} -> {output_path}")

# Process all files in data directory
for file in os.listdir(DATA_DIR):
    if file.endswith(".csv"):  # Adjust for other formats if needed
        clean_dataset(os.path.join(DATA_DIR, file))