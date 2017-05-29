from Food import Food

class FoodDB:
    def __init__(self, path):
        self.filePath = path

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