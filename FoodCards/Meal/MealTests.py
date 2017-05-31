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
        nutri = self.meal.getMealNutricion()
        self.assertEqual(nutri, ["Summary", 250, 700, 17.5, 0, 0, 0, 40, 63, 0, 0])

    def test_nutricionPercentDistribution(self):
        nutriPercentage = self.meal.getNutricionPercentDistibution()
        self.assertEqual(nutriPercentage, [33.2,52.3,14.5])

    def test_nutricionPer100g(self):
        nutricionPer100g = self.meal.getNutricionPer100g()
        self.assertEqual(nutricionPer100g, [16, 25.2, 7])

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
        self.kurczakPath = "Recipies/test_Kurczak z ryzem.txt"