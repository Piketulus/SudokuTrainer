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

    def get_all_by_name(self, name):

        return self._statistic_repository.find_all_by_name(name)

    def get_all_by_maxtime(self, maxtime):

        return self._statistic_repository.find_all_by_maxtime(maxtime)

    def get_all_by_difficulty(self, difficulty):

        return self._statistic_repository.find_all_by_difficulty(difficulty)


statistic_service = StatisticService()
