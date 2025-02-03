from google.cloud import bigquery
import google.api_core.exceptions

def analyze_data(project_id, dataset_id, table_id):
    """Analyzes data in a BigQuery table.

    Connects to BigQuery, queries the specified table for 
    the number of rows, and prints the result.

    Args:
        project_id: The ID of your Google Cloud project.
        dataset_id: The ID of the dataset containing the table.
        table_id: The ID of the table to analyze.

    Raises:
        google.api_core.exceptions.BadRequest: If the query is invalid.
        google.api_core.exceptions.NotFound: If the table is not found.
        Exception: For any other error during BigQuery interaction.
    """
    try:
        client = bigquery.Client(project=project_id)

        query = f"""
            SELECT COUNT(*) AS num_rows
            FROM `{project_id}.{dataset_id}.{table_id}`
        """

        query_job = client.query(query)
        results = query_job.result()  # Waits for the query to complete

        for row in results:
            print(f"Number of rows in table: {row.num_rows}")

    except google.api_core.exceptions.BadRequest as e:
        print(f"Invalid query: {e}")
        raise  # Re-raise the exception after printing the error
    except google.api_core.exceptions.NotFound as e:
        print(f"Table not found: {e}")
        raise  # Re-raise the exception after printing the error
    except Exception as e:
        print(f"An error occurred: {e}")
        raise  # Re-raise the exception after printing the error
