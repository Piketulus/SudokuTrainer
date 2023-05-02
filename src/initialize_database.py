from database_connection import get_database_connection


def drop_tables(connection):
    """
    Drop tables if they exist.

    Args:
        connection: connection to the database
    """

    cursor = connection.cursor()

    cursor.execute("""
        drop table if exists stats;
    """)

    connection.commit()


def create_tables(connection):
    """
    Create tables to store statistics.

    Args:
        connection: connection to the database
    """

    cursor = connection.cursor()

    cursor.execute("""
        create table stats (
            name text,
            time real,
            difficulty integer,
            date text
        );
    """)

    connection.commit()


def initialize_database():
    """
    Initialize the database by dropping and creating tables.
    """

    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
