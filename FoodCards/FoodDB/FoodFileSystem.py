import os.path
from Food.Food import Food
from TextFormatter.TextFormatter import TextFormatter

class FoodFileSystem:
    def __init__(self, path):
        self.filePath = path
        self.ensureFileExists(self.filePath)

    def isPresent(self, name):
        name += ';'
        if(self.findFood(name) != None):
            return True
        else:
            return False

    def findFood(self, name):
        food = None
        file = open(self.filePath)
        for line in file:
            lineLower = line.lower()
            nameLower = name.lower()
            if (lineLower.find(nameLower) > -1):
                food = self.loadFood(line)
                break
        file.close()
        return food

    def loadFood(self, line):
        food = Food()
        foodParts = line.split(";")
        for i in range(len(foodParts)):
            if(foodParts[i] == ''):
                foodParts[i] = '0'
        food.name = foodParts[0]
        food.kcal = float(foodParts[1])
        food.prot = float(foodParts[2])
        food.fat = float(foodParts[3])
        food.fat_sat = float(foodParts[4])
        food.fat_unsat_mono = float(foodParts[5])
        food.fat_unsat_bi = float(foodParts[6])
        food.carb = float(foodParts[7])
        food.carb_sugar = float(foodParts[8])
        food.fiber = float(foodParts[9])
        return food

    def getFood(self, name):
        food = self.findFood(name)
        return food

    def addFood(self, food):
        with open(self.filePath, 'a') as file:
            csvFoodLine = self.createDBLineFromFoodValues(food)
            file.write(csvFoodLine)

    def saveToFile(self, meal):
        self.ensureDirectoryExists("Recipies")
        filePath = "Recipies/" + meal.name + ".txt"
        file = open(filePath, 'w')

        file.write(meal.name + '\n')
        file.write(' \n')
        lf = TextFormatter(8)
        columnNames = ["size", "kcal", "fat", "fatS", "fatUsM", "fatUsB", "prot", "carb", "carbS", "fiber"]
        line = lf.createColumnNames(columnNames)
        file.write(line)
        for ingr in meal.ingridients:
            file.write(lf.createColumnValues(ingr.getFoodNutricion()))

        file.write("\n" + '-'*100 + '\n')
        file.write(lf.createColumnValues(meal.getMealNutricion()))

        distr = meal.getNutricionPercentDistibution()
        file.write('\n' + "% distribution:\nprot:\t" + str(distr[0]) + "\ncarb:\t" + str(distr[1]) + "\nfat: \t" + str(distr[2]) + '\n')

        nutriPer100g = meal.getNutricionPer100g()
        file.write('\n' + "Nutri in 100g:\nprot:\t" + str(nutriPer100g[0]) + "g\ncarb:\t" + str(nutriPer100g[1]) + "g\nfat: \t" + str(nutriPer100g[2]) +'g\n')

        file.close()

    def ensureDirectoryExists(self, name):
        dir = os.path.dirname(name)
        if(not os.path.exists(name)):
            os.makedirs(name)

    def ensureFileExists(self, path):
        if(not os.path.isfile(path)):
            file = open(path, 'x')
            file.close()

    def createDBLineFromFoodValues(self, food):
        foodVal = food.getFoodNutricionPer100g()
        line = "{};{};{};{};".format(foodVal[0], foodVal[2], foodVal[3], foodVal[4])
        line += "{};{};{};{};".format(foodVal[5], foodVal[6], foodVal[7], foodVal[8])
        line += "{};{};\n".format(foodVal[9], foodVal[10])
        return line