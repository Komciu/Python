import unittest
import os
from Meal.Meal import Meal
from Food.Food import Food

class MealTests(unittest.TestCase):
    def test_createMeal(self):
        self.assertEqual(self.meal.name, "test_Kurczak z ryzem")

    def test_addFood(self):
        self.assertEqual(2, self.meal.getIngridiensCount())

    def test_calculateNutricionValue(self):
        self.assertEqual(700, self.meal.summary().kcal)

    def test_mealNutricion(self):
        nutri = self.meal.getMealNutricion()
        self.assertEqual(nutri, ["Summary", 250, 700, 17.5, 0, 0, 0, 40, 63, 0, 0])

    def test_nutricionPercentDistribution(self):
        nutriPercentage = self.meal.getNutricionPercentDistibution()
        self.assertEqual(nutriPercentage, [33.2,52.3,14.5])

    def test_saveMealToFileAndCheckTitle(self):
        self.meal.saveToFile()
        f = open("Recipies/test_Kurczak z ryzem.txt")
        title = f.readline()
        f.close()
        self.assertEqual(title, self.meal.name + '\n')
        os.remove("Recipies/test_Kurczak z ryzem.txt")

    def test_saveMealToFileAndCheckLineCount(self):
        self.meal.saveToFile()
        f = open("Recipies/test_Kurczak z ryzem.txt")
        lineCounter = 0
        for line in f:
            lineCounter = lineCounter + 1
        f.close()
        self.assertEqual(lineCounter, 13)
        os.remove("Recipies/test_Kurczak z ryzem.txt")

    def test_fileParameterRow(self):
        self.meal.saveToFile()

        f = open("Recipies/test_Kurczak z ryzem.txt")
        f.readline()
        f.readline()

        line = f.readline()
        f.close()
        self.assertEqual(line, "                size    kcal    fat     fatS    fatUsM  fatUsB  prot    carb    carbS   fiber   \n")
        os.remove("Recipies/test_Kurczak z ryzem.txt")

    def prepareMeal(self):
        meal = Meal("test_Kurczak z ryzem")
        f1 = Food("kurczak")
        f1.kcal = 200
        f1.fat = 5
        f1.prot = 20
        f1.carb = 2
        f1.portion = 150
        f2 = Food("ryz")
        f2.kcal = 400
        f2.fat = 10
        f2.prot = 10
        f2.carb = 60
        meal.addFood(f1)
        meal.addFood(f2)
        return meal

    def setUp(self):
        self.meal = self.prepareMeal()