from entities.statistic import Statistic
from database_connection import get_database_connection


def get_stat_by_row(row):
    return Statistic(row["name"], row["time"], row["date"]) if row else None


class StatisticRepository:

    def __init__(self, connection):

        self._connection = connection

    def find_all(self):

        cursor = self._connection.cursor()
        cursor.execute("select * from users")
        rows = cursor.fetchall()
        return list(map(get_stat_by_row, rows))

    def find_all_by_name(self, name):

        cursor = self._connection.cursor()
        cursor.execute(
            "select * from users where name = ?",
            (name,)
        )
        rows = cursor.fetchall()
        return list(map(get_stat_by_row, rows))
    
    def find_all_by_maxtime(self, maxtime):
            
        cursor = self._connection.cursor()
        cursor.execute(
            "select * from users where time <= ?",
            (maxtime,)
        )
        rows = cursor.fetchall()
        return list(map(get_stat_by_row, rows))

    def create(self, statistic):

        cursor = self._connection.cursor()
        cursor.execute(
            "insert into users (name, time, date) values (?, ?, ?)",
            (statistic.name, statistic.time, statistic.date)
        )
        self._connection.commit()

    def delete_all(self):

        cursor = self._connection.cursor()
        cursor.execute("delete from stats")
        self._connection.commit()


statistic_repository = StatisticRepository(get_database_connection())