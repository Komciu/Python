import unittest
from Food.Food import Food

class FoodTests(unittest.TestCase):
    def test_createFood(self):
        f1 = self.prepareFood()
        f2 = self.prepareFood()
        f3 = f1 + f2
        self.assertEqual(f3.kcal, 200)
        self.assertEqual(f3.fat_sat, 6)
        self.assertEqual(f3.prot, 6)
        self.assertEqual(f3.fiber, 14)

    def test_addScaledPortion(self):
        f1 = Food()
        f2 = self.prepareFood()
        f2.portion = 200
        f1.addPortion(f2)
        self.assertEqual(f1.kcal, 200)

    def test_getFoodNutricion(self):
        f = self.prepareFood()
        resultWanted = ["", 100 ,100, 3, 10, 3, 5, 2, 20, 5, 7]
        self.assertEqual(resultWanted, f.getFoodNutricion())

    def test_getFoodNutricionWithBiggerPortion(self):
        f = self.prepareFood()
        f.portion = 200
        resultWanted = ["", 200, 200, 6, 20, 6, 10, 4, 40, 10, 14]
        self.assertEqual(resultWanted, f.getFoodNutricion())

    def test_getFoodNutricionWithoutPortion(self):
        f = self.prepareFood()
        f.portion = 200
        resultWanted = ["", 100, 100, 3, 10, 3, 5, 2, 20, 5, 7]
        self.assertEqual(resultWanted, f.getFoodNutricionPer100g())

    def test_addPortion(self):
        f1 = self.prepareFood()
        f2 = self.prepareFood()
        f = Food("summary")
        f.portion = 0
        f.addPortion(f1)
        self.assertEqual(f.portion, 100)
        self.assertEqual(f.kcal, 100)
        self.assertEqual(f.carb, 20)

    def test_add2Portions(self):
        f1 = self.prepareFood()
        f2 = self.prepareFood()
        f = Food("summary")
        f.portion = 0
        f.addPortion(f1)
        f.addPortion(f2)
        self.assertEqual(f.portion, 200)
        self.assertEqual(f.kcal, 200)
        self.assertEqual(f.carb, 40)
        self.assertEqual(f1.portion, 100)
        self.assertEqual(f1.kcal, 100)
        self.assertEqual(f1.carb, 20)
        self.assertEqual(f2.portion, 100)
        self.assertEqual(f2.kcal, 100)
        self.assertEqual(f2.carb, 20)

    def test_comparision(self):
        f1 = self.prepareFood()
        f2 = self.prepareFood()

        self.assertTrue(f1 == f2)


    def prepareFood(self):
        f = Food("")
        f.kcal = 100
        f.fat = 10
        f.fat_unsat_mono = 5
        f.fat_unsat_bi = 2
        f.fat_sat = 3
        f.prot = 3
        f.carb = 20
        f.carb_sugar = 5
        f.fiber = 7
        return f