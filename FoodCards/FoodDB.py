import os.path
from Food import Food

class FoodDB:
    def __init__(self, path):
        self.filePath = path
        self.ensureFileExists(self.filePath)

    def isPresent(self, name):
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

    def ensureFileExists(self, path):
        if(not os.path.isfile(path)):
            file = open(path, 'x')
            file.close()

    def createDBLineFromFoodValues(self, food):
        foodVal = food.getFoodNutricionPer100g()
        line = "{};{};{};{};".format(foodVal[0], foodVal[2], foodVal[3], foodVal[4])
        line += "{};{};{};{};".format(foodVal[5], foodVal[6], foodVal[7], foodVal[8])
        line += "{};{};{};".format(foodVal[9], foodVal[10], foodVal[10])
        return line