from Food import Food
from TextFormatter import TextFormatter
from FoodDB import FoodDB

class Meal:
    def __init__(self, name):
        self.name = name
        self.ingridients = []

    def addFood(self, food):
        self.ingridients.append(food)

    def getIngridiensCount(self):
        return self.ingridients.__len__()

    def getIngridients(self):
        return self.ingridients

    def summary(self):
        f = Food("Summary")
        for food in self.ingridients:
            f.addPortion(food)
            f.portion += food.portion
        return f

    def getMealNutricion(self):
        summary = self.summary()
        return [summary.name,
                summary.portion,
                summary.kcal,
                summary.fat,
                summary.fat_unsat_mono,
                summary.fat_unsat_bi,
                summary.fat_sat,
                summary.prot,
                summary.carb,
                summary.carb_sugar,
                summary.fiber]

    def saveToFile(self):
        filePath = self.name + ".txt"
        file = open(filePath, 'w')

        file.write(self.name + '\n')
        file.write(' \n')
        lf = TextFormatter(8)
        columnNames = ["size", "kcal", "fat", "fatS", "fatUsM", "fatUsB", "prot", "carb", "carbS", "fiber"]
        line = lf.createColumnNames(columnNames)
        file.write(line)
        for ingr in self.ingridients:
            file.write(lf.createColumnValues(ingr.getFoodNutricion()))

        file.write("\n" + '-'*100 + '\n')
        file.write(lf.createColumnValues(self.getMealNutricion()))

        file.close()
