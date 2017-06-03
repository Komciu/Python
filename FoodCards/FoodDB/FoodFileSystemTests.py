import unittest
import os.path
from FoodDB.FoodFileSystem import FoodFileSystem
from Food.Food import Food
from Meal.Meal import Meal

class FoodFileSystemTests(unittest.TestCase):
    def test_isFoodPresent(self):
        self.assertEqual(True, self.fdb.isPresent("Testing"))

    def test_letterSizeDoesNotMatter(self):
        self.assertEqual(True, self.fdb.isPresent("TeSTinG"))

    def test_foodDoesNotExist(self):
        self.assertFalse(self.fdb.isPresent("test"))

    def test_getNutricion(self):
        self.assertEqual(["Testing", 1, 100, 2, 3, 4, 5, 6, 7, 8, 9.10], self.fdb.getFood("testing").getFoodNutricion())

    def test_dontCrashOnLackingValues(self):
        self.assertEqual(1, self.fdb.getFood("lacking").kcal)

    def test_createNutricionFile(self):
        fdb = FoodFileSystem("tempFoodCsv.csv")
        self.assertTrue(os.path.isfile("tempFoodCsv.csv"))
        os.remove("tempFoodCsv.csv")

    def test_addFood(self):
        fdb = FoodFileSystem("tempFoodCsv2.csv")
        food = Food("addedFood")
        fdb.addFood(food)
        food = Food("addedFood2")
        fdb.addFood(food)
        self.assertTrue(fdb.isPresent("addedFood"))
        self.assertTrue(fdb.isPresent("addedFood2"))
        self.assertFalse(fdb.isPresent("addedFood3"))
        os.remove("tempFoodCsv2.csv")

    def test_fileParameterRow(self):
        self.fdb.saveToFile(self.meal)

        f = open(self.kurczakPath)
        f.readline()
        f.readline()

        line = f.readline()
        f.close()
        self.assertEqual(line, "                size    kcal    fat     fatS    fatUsM  fatUsB  prot    carb    carbS   fiber   \n")

    def test_saveMealToFileAndCheckTitle(self):
        self.fdb.saveToFile(self.meal)
        f = open(self.kurczakPath)
        title = f.readline()
        f.close()
        self.assertEqual(title, self.meal.name + '\n')

    def test_savesValuesPer100g(self):
        self.fdb.saveToFile(self.meal)
        nutriPer100gLines = self.loadValuesPer100g()

        protLine = nutriPer100gLines[0]
        carbLine = nutriPer100gLines[1]
        fatLine = nutriPer100gLines[2]
        self.assertEqual(protLine, "prot:\t16.0g\n")
        self.assertEqual(carbLine, "carb:\t25.2g\n")
        self.assertEqual(fatLine, "fat: \t7.0g\n")

    def prepareMeal(self):
        meal = Meal("test_Kurczak z ryzem")
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

    def loadValuesPer100g(self):
        nutriPer100gLines = []
        relatedLines = 0
        f = open(self.kurczakPath)
        for line in f:
            if (relatedLines > 0):
                nutriPer100gLines.append(line)
            relatedLines -= 1
            if (line.find("Nutri in 100g:") > -1):
                relatedLines = 3
        f.close()
        return nutriPer100gLines

    def setUp(self):
        self.fdb = FoodFileSystem("testCsv.csv")
        self.meal = self.prepareMeal()
        self.kurczakPath = "Recipies/test_Kurczak z ryzem.txt"

    def tearDown(self):
        if (os.path.isfile(self.kurczakPath)):
            os.remove(self.kurczakPath)
