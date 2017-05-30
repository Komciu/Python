import unittest
import os.path
from FoodDB import FoodDB
from Food import Food

class FoodDBTests(unittest.TestCase):
    def test_isFoodPresent(self):
        fdb = FoodDB("testCsv.csv")
        self.assertEqual(True, fdb.isPresent("Testing"))
        self.assertEqual(True, fdb.isPresent("TeSTinG"))

    def test_getNutricion(self):
        fdb = FoodDB("testCsv.csv")
        self.assertEqual(["Testing", 100, 1, 2, 3, 4, 5, 6, 7, 8, 9.10], fdb.getFood("testing").getFoodNutricion())

    def test_dontCrashOnLackingValues(self):
        fdb = FoodDB("testCsv.csv")
        self.assertEqual(1, fdb.getFood("lacking").kcal)

    def test_createNutricionFile(self):
        fdb = FoodDB("tempFoodCsv.csv")
        self.assertTrue(os.path.isfile("tempFoodCsv.csv"))
        os.remove("tempFoodCsv.csv")

    def test_addFood(self):
        fdb = FoodDB("tempFoodCsv2.csv")
        food = Food("addedFood")
        fdb.addFood(food)
        self.assertTrue(fdb.isPresent("addedFood"))
        os.remove("tempFoodCsv2.csv")