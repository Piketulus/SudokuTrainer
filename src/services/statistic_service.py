from entities.statistic import Statistic

from repositories.statistic_repository import (
    statistic_repository as default_statistic_repository
)


class StatisticService:

    def __init__(self, statistic_repository=default_statistic_repository):

        self._statistic_repository = statistic_repository

    def create_statistic(self, name, time, difficulty, date):

        statistic = Statistic(name, time, difficulty, date)
        self._statistic_repository.create(statistic)

    def get_all(self):

        return self._statistic_repository.find_all()

    def get_all_by_filter(self, name, maxtime, difficulty):

        return self._statistic_repository.find_all_by_filter(name, maxtime, difficulty)


statistic_service = StatisticService()
