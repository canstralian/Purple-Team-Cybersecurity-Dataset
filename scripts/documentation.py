import os

# Generate README file with dataset description
def generate_readme(dataset_name: str, description: str, columns: list) -> None:
    """
    Generates a README file for the dataset, including a description and column details.

    Args:
    - dataset_name (str): The name of the dataset.
    - description (str): Description of the dataset.
    - columns (list): List of columns with descriptions.
    """
    readme_content = f"# {dataset_name}\n\n"
    readme_content += f"## Description\n{description}\n\n"
    readme_content += "## Columns\n"
    
    for column, col_description in columns:
        readme_content += f"- {column}: {col_description}\n"

    # Save README.md file
    with open(f"{dataset_name}/README.md", "w") as f:
        f.write(readme_content)
    
    print(f"README generated for {dataset_name}")

# Create a script for generating dataset-specific documentation
def generate_dataset_docs(df, dataset_name: str) -> None:
    """
    Generates a dataset documentation file with basic info such as column types.

    Args:
    - df (pd.DataFrame): The dataset.
    - dataset_name (str): The name of the dataset.
    """
    columns_info = [(col, df[col].dtype) for col in df.columns]
    
    generate_readme(dataset_name, "A dataset for modeling purposes.", columns_info)