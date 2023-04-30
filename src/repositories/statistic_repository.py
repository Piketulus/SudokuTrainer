from entities.statistic import Statistic
from database_connection import get_database_connection


def get_stat_by_row(row):
    return Statistic(row["name"], row["time"], row["difficulty"], row["date"]) if row else None


class StatisticRepository:

    def __init__(self, connection):

        self._connection = connection

    def find_all(self):

        cursor = self._connection.cursor()
        cursor.execute("select * from stats")
        rows = cursor.fetchall()
        return list(map(get_stat_by_row, rows))

    def find_all_by_filter(self, name, maxtime, difficulty):

        name = "%" + name + "%"

        cursor = self._connection.cursor()

        if difficulty == "All":
            cursor.execute(
                "select * from stats where name like ? and time <= ?",
                (name, maxtime)
            )
        else:
            cursor.execute(
                "select * from stats where name like ? and time <= ? and difficulty = ?",
                (name, maxtime, difficulty)
            )
        rows = cursor.fetchall()
        return list(map(get_stat_by_row, rows))

    def create(self, statistic):

        cursor = self._connection.cursor()
        cursor.execute(
            "insert into stats (name, time, difficulty, date) values (?, ?, ?, ?)",
            (statistic.name, statistic.time, statistic.difficulty, statistic.date)
        )
        self._connection.commit()

    def delete_all(self):

        cursor = self._connection.cursor()
        cursor.execute("delete from stats")
        self._connection.commit()


statistic_repository = StatisticRepository(get_database_connection())
