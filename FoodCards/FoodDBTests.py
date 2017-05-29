import unittest
from FoodDB import FoodDB

class FoodDBTests(unittest.TestCase):
    def test_isFoodPresent(self):
        fdb = FoodDB("testCsv.csv")
        self.assertEqual(True, fdb.isPresent("Testing"))
        self.assertEqual(True, fdb.isPresent("TeSTinG"))

    def test_getNutricion(self):
        fdb = FoodDB("testCsv.csv")
        self.assertEqual(["Testing", 100, 1, 3, 5, 6, 4, 2, 7, 8, 9.10], fdb.getFood("testing").getFoodNutricion())

    def test_lackingValues(self):
        fdb = FoodDB("testCsv.csv")
        self.assertEqual(1, fdb.getFood("lacking").kcal)