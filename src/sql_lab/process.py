import os
import logging
import pandas as pd
import mysql.connector


# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Read database connection information from environment variables
DBHOST = os.getenv("DBHOST")
DBNAME = os.getenv("DBNAME")
DBUSER = os.getenv("DBUSER")
DBPASS = os.getenv("DBPASS")


def read_data(filename):
    """Load a CSV file into a pandas DataFrame."""
    logger.info("Reading data from %s", filename)

    data = pd.read_csv(filename)

    logger.info("Loaded %d rows", len(data))
    return data


def clean_data(data):
    """Remove rows with missing values and return the cleaned DataFrame."""
    logger.info("Cleaning data")

    # Remove rows that contain missing values
    data = data.dropna()

    logger.info("Data cleaned. %d rows remain", len(data))
    return data


def load_data(data, table):
    """Create the MySQL table if needed and upload the DataFrame."""
    logger.info("Loading data into table %s", table)

    # Connect to the MySQL database
    connection = mysql.connector.connect(
        host=DBHOST,
        database=DBNAME,
        user=DBUSER,
        password=DBPASS
    )

    cursor = connection.cursor()

    # Create the table using the columns from the DataFrame
    columns = []
    for column in data.columns:
        columns.append(f"`{column}` TEXT")

    create_table = f"""
    CREATE TABLE IF NOT EXISTS `{table}` (
        {", ".join(columns)}
    )
    """

    cursor.execute(create_table)

    # Insert each row into the table
    column_names = ", ".join(f"`{column}`" for column in data.columns)
    placeholders = ", ".join(["%s"] * len(data.columns))

    insert_query = f"""
    INSERT INTO `{table}` ({column_names})
    VALUES ({placeholders})
    """

    for row in data.itertuples(index=False, name=None):
        cursor.execute(insert_query, row)

    connection.commit()

    logger.info("Uploaded %d rows to %s", len(data), table)

    cursor.close()
    connection.close()


def main():
    """Read, clean, and load the CSV data into MySQL."""
    logger.info("Starting data processing")

    # Read the CSV file
    data = read_data("MOCK_DATA.csv")

    # Clean the data
    data = clean_data(data)

    # Always use mock as the destination table
    load_data(data, "mock")

    logger.info("Data processing complete")


if __name__ == "__main__":
    main()