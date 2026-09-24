import os
import logging
import mysql.connector

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Read database credentials from environment variables
DBHOST = os.getenv("DBHOST")
DBNAME = os.getenv("DBNAME")
DBUSER = os.getenv("DBUSER")
DBPASS = os.getenv("DBPASS")


def get_data_by_group(value):
    """Retrieve rows from the mock table where the group column equals value."""
    logger.info("Getting rows where group = %s", value)

    connection = mysql.connector.connect(
        host=DBHOST,
        database=DBNAME,
        user=DBUSER,
        password=DBPASS
    )

    cursor = connection.cursor()

    # Use a parameterized query to safely filter by group
    query = """
    SELECT *
    FROM mock
    WHERE `group` = %s
    """

    cursor.execute(query, (value,))
    results = cursor.fetchall()

    logger.info("Retrieved %d rows", len(results))

    cursor.close()
    connection.close()

    return results


def plot_counts(groupby):
    """Count rows in mock grouped by the specified column."""
    logger.info("Counting rows grouped by %s", groupby)

    connection = mysql.connector.connect(
        host=DBHOST,
        database=DBNAME,
        user=DBUSER,
        password=DBPASS
    )

    cursor = connection.cursor()

    # Column names cannot be parameterized, so safely quote the column name.
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
    connection.close()

    return results


def main():
    """Run the query functions and print their results."""
    # Demonstrate filtering rows by the group column
    group_results = get_data_by_group("A")
    print("Rows where group = A:")
    for row in group_results:
        print(row)

    # Demonstrate counting rows by another column
    color_counts = plot_counts("color")
    print("\nCounts by color:")
    for color, count in color_counts:
        print(color, count)


if __name__ == "__main__":
    main()