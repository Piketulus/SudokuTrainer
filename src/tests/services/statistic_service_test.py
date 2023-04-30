import unittest
from services.statistic_service import statistic_service
from repositories.statistic_repository import statistic_repository


class TestStatisticRepository(unittest.TestCase):
    def setUp(self):
        statistic_repository.delete_all()

    def test_create_statistic(self):
        statistic_service.create_statistic("Joel", 100, "5", "2021-05-05")
        stats = statistic_service.get_all()

        self.assertEqual(len(stats), 1)
        self.assertEqual(stats[0].name, "Joel")

    def test_get_all(self):
        statistic_service.create_statistic("Joel", 100, "5", "2021-05-05")
        statistic_service.create_statistic("Kalle", 200, "6", "2021-05-05")
        stats = statistic_service.get_all()

        self.assertEqual(len(stats), 2)
        self.assertEqual(stats[0].name, "Joel")
        self.assertEqual(stats[1].name, "Kalle")

    def test_get_all_by_filter(self):
        statistic_service.create_statistic("Joel", 100, "5", "2021-05-05")
        statistic_service.create_statistic("Kalle", 200, "6", "2021-05-05")
        stats = statistic_service.get_all_by_filter("Jo", 150, "5")

        self.assertEqual(len(stats), 1)
        self.assertEqual(stats[0].name, "Joel")

    def test_get_all_by_filter_none(self):
        statistic_service.create_statistic("Joel", 100, "5", "2021-05-05")
        statistic_service.create_statistic("Kalle", 200, "6", "2021-05-05")
        stats = statistic_service.get_all_by_filter("Joel", 50, "All")

        self.assertEqual(len(stats), 0)
        