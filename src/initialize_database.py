from database_connection import get_database_connection


def drop_tables(connection):

    cursor = connection.cursor()

    cursor.execute("""
        drop table if exists stats;
    """)

    connection.commit()


def create_tables(connection):

    cursor = connection.cursor()

    cursor.execute("""
        create table stats (
            name text,
            time real,
            date text
        );
    """)

    connection.commit()


def initialize_database():

    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
