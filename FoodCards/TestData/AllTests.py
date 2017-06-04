import unittest
from Food.FoodTests import FoodTests
from FoodDB.FoodFileSystemTests import FoodFileSystemTests
from Meal.MealTests import MealTests
from Meal.Meal import Meal
from Food.Food import Food
from FoodDB.FoodFileSystem import FoodFileSystem

def prepareMeal():
    meal = Meal("demo")
    f1 = Food("kurczak")
    f1.kcal = 200
    f1.fat = 5
    f1.prot = 20
    f1.carb = 2
    f1.size = 150
    f2 = Food("ryz")
    f2.kcal = 400
    f2.fat = 10
    f2.prot = 10
    f2.carb = 60
    meal.addFood(f1)
    meal.addFood(f2)
    return meal

def demo():
    meal = prepareMeal()
    fdb = FoodFileSystem("demoNutri.txt")
    fdb.saveToFile(meal)

if __name__ == '__main__':
    demo()
    unittest.main()
