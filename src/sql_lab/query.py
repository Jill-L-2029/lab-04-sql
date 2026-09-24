import os
import logging
import mysql.connector

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)
logger = logging.getLogger(__name__)

# Read database credentials from environment variables
DBHOST = os.getenv("DBHOST")
DBNAME = os.getenv("DBNAME")
DBUSER = os.getenv("DBUSER")
DBPASS = os.getenv("DBPASS")


def get_data_by_group(value):
    """Retrieve all rows from mock where the group column equals value."""
    logger.info("Getting rows where group = %s", value)

    connection = None

    try:
        # Connect to the user's database
        connection = mysql.connector.connect(
            host=DBHOST,
            database=DBNAME,
            user=DBUSER,
            password=DBPASS,
        )

        cursor = connection.cursor()

        # Use a parameterized query to filter by group
        query = """
        SELECT *
        FROM mock
        WHERE `group` = %s
        """

        cursor.execute(query, (value,))
        results = cursor.fetchall()

        logger.info("Retrieved %d rows", len(results))

        cursor.close()
        return results

    except mysql.connector.Error as err:
        logger.error("Database error: %s", err)
        raise

    finally:
        # Close the database connection
        if connection is not None and connection.is_connected():
            connection.close()
            logger.info("Database connection closed")


def plot_counts(groupby):
    """Count rows in mock grouped by the specified column."""
    logger.info("Counting rows grouped by %s", groupby)

    # Only allow columns that actually exist in the mock table
    allowed_columns = {
        "id",
        "group",
        "in_stock",
        "color",
        "isbn",
        "city",
    }

    if groupby not in allowed_columns:
        raise ValueError(f"Invalid column name: {groupby}")

    connection = None

    try:
        # Connect to the user's database
        connection = mysql.connector.connect(
            host=DBHOST,
            database=DBNAME,
            user=DBUSER,
            password=DBPASS,
        )

        cursor = connection.cursor()

        # Column names cannot be parameterized, so quote the column name
        query = f"""
        SELECT `{groupby}`, COUNT(*) AS count
        FROM mock
        GROUP BY `{groupby}`
        ORDER BY count DESC
        """

        cursor.execute(query)
        results = cursor.fetchall()

        logger.info("Retrieved counts for %d groups", len(results))

        cursor.close()
        return results

    except mysql.connector.Error as err:
        logger.error("Database error: %s", err)
        raise

    finally:
        # Close the database connection
        if connection is not None and connection.is_connected():
            connection.close()
            logger.info("Database connection closed")


def main():
    """Run the query functions and print their results."""

    # Get rows for one group value
    group_results = get_data_by_group("cat")

    print("Rows where group = cat:")
    for row in group_results:
        print(row)

    # Count rows by color
    color_counts = plot_counts("color")

    print("\nCounts by color:")
    for color, count in color_counts:
        print(color, count)


if __name__ == "__main__":
    main()