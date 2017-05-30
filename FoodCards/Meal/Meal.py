from Food.Food import Food
from TextFormatter.TextFormatter import TextFormatter
import os

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
        f.portion = 0
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

    def getNutricionPercentDistibution(self):
        summary = self.summary()
        sum = summary.prot + summary.carb + summary.fat
        protPercentage = round((summary.prot / sum)*100, 1)
        carbPercentage = round((summary.carb / sum)*100, 1)
        fatPercentage = round((summary.fat / sum)*100, 1)
        return [protPercentage, carbPercentage, fatPercentage]

    def saveToFile(self):
        self.ensureDirectoryExists("Recipies")
        filePath = "Recipies/" + self.name + ".txt"
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

        distr = self.getNutricionPercentDistibution()
        file.write('\n' + "% distribution:\nprot:\t" + str(distr[0]) + "\ncarb:\t" + str(distr[1]) + "\nfat: \t" + str(distr[2]))

        file.close()

    def ensureDirectoryExists(self, name):
        dir = os.path.dirname(name)
        if(not os.path.exists(name)):
            os.makedirs(name)