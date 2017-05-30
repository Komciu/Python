import unittest
from Meal import Meal
from Food import Food

class MealTests(unittest.TestCase):
    def test_createMeal(self):
        meal = self.prepareMeal()
        self.assertEqual(meal.name, "Kurczak z ryzem")

    def test_addFood(self):
        meal = self.prepareMeal()
        self.assertEqual(2, meal.getIngridiensCount())

    def test_calculateNutricionValue(self):
        meal = self.prepareMeal()
        self.assertEqual(700, meal.summary().kcal)

    def test_mealNutricion(self):
        meal = self.prepareMeal()
        nutri = meal.getMealNutricion()
        self.assertEqual(nutri, ["Summary", 250, 700, 17.5, 0, 0, 0, 40, 63, 0, 0])

    def test_nutricionPercentDistribution(self):
        meal = self.prepareMeal()
        nutriPercentage = meal.getNutricionPercentDistibution()
        self.assertEqual(nutriPercentage, [33.2,52.3,14.5])

    def test_saveMealToFileAndCheckTitle(self):
        meal = self.prepareMeal()
        self.cleanKurczakFile()
        meal.saveToFile()
        f = open("Kurczak z ryzem.txt")
        title = f.readline()
        f.close()
        self.assertEqual(title, meal.name + '\n')

    def test_saveMealToFileAndCheckLineCount(self):
        meal = self.prepareMeal()
        self.cleanKurczakFile()
        meal.saveToFile()
        f = open("Kurczak z ryzem.txt")
        lineCounter = 0
        for line in f:
            lineCounter = lineCounter + 1
        f.close()
        self.assertEqual(lineCounter, 13)

    def test_fileParameterRow(self):
        meal = self.prepareMeal()
        self.cleanKurczakFile()
        meal.saveToFile()

        f = open("Kurczak z ryzem.txt")
        f.readline()
        f.readline()

        line = f.readline()
        f.close()
        self.assertEqual(line, "                size    kcal    fat     fatS    fatUsM  fatUsB  prot    carb    carbS   fiber   \n")

    def prepareMeal(self):
        meal = Meal("Kurczak z ryzem")
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

    def cleanKurczakFile(self):
        f = open("Kurczak z ryzem.txt", 'w')
        f.close()
