import unittest
from repositories.statistic_repository import statistic_repository
from entities.statistic import Statistic


class TestStatisticRepository(unittest.TestCase):
    def setUp(self):
        statistic_repository.delete_all()
        self.stat_joel = Statistic("Joel", 100, "5", "2021-05-05")
        self.stat_kalle = Statistic("Kalle", 200, "6", "2021-05-05")

    def test_create(self):
        statistic_repository.create(self.stat_joel)
        stats = statistic_repository.find_all()

        self.assertEqual(len(stats), 1)
        self.assertEqual(stats[0].name, self.stat_joel.name)

    def test_find_all(self):
        statistic_repository.create(self.stat_joel)
        statistic_repository.create(self.stat_kalle)
        stats = statistic_repository.find_all()

        self.assertEqual(len(stats), 2)
        self.assertEqual(stats[0].name, self.stat_joel.name)
        self.assertEqual(stats[1].name, self.stat_kalle.name)

    def test_find_all_by_filter(self):
        statistic_repository.create(self.stat_joel)
        statistic_repository.create(self.stat_kalle)
        stats = statistic_repository.find_all_by_filter("Jo", 150, "5")

        self.assertEqual(len(stats), 1)
        self.assertEqual(stats[0].name, self.stat_joel.name)

    def test_find_all_by_filter_none(self):
        statistic_repository.create(self.stat_joel)
        statistic_repository.create(self.stat_kalle)
        stats = statistic_repository.find_all_by_filter("Joel", 50, "All")

        self.assertEqual(len(stats), 0)
