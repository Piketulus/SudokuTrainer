from entities.statistic import Statistic

from repositories.statistic_repository import (
    statistic_repository as default_statistic_repository
)


class StatisticService:
    """
    Class responsible for handling the logic of the statistics.
    """

    def __init__(self, statistic_repository=default_statistic_repository):
        """
        Class constructor that initializes the StatisticRepository.

        Args:
            statistic_repository: The StatisticRepository to use
        """

        self._statistic_repository = statistic_repository

    def create_statistic(self, name, time, difficulty, date):
        """
        Creates a statistic object in the database.

        Args:
            name: Name of the user who solved the puzzle
            time: Time taken to solve the puzzle in seconds
            difficulty: Difficulty of the puzzle
            date: Date of completion of the puzzle
        """

        statistic = Statistic(name, time, difficulty, date)
        self._statistic_repository.create(statistic)

    def get_all(self):
        """
        Get all statistic objects.


        Returns: 
            list of Statistic objects
        """

        return self._statistic_repository.find_all()

    def get_all_by_filter(self, name, maxtime, difficulty):
        """
        Get all statistical objects by filter.

        Args:
            name: Name of the statistic to look for
            maxtime: Maximum time to look for the statistic in seconds
            difficulty: Difficulty of the statistic to look for

        Returns: 
            List of Statistic objects that match the filter or 
            empty list if none match is found in the repository
        """

        return self._statistic_repository.find_all_by_filter(name, maxtime, difficulty)


statistic_service = StatisticService()
