from Food.Food import Food
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

    def getNutricionPer100g(self):
        summary = self.summary()
        sum = summary.prot + summary.carb + summary.fat
        protPer100g = round((summary.prot / (summary.portion/100)), 1)
        carbPer100g = round((summary.carb / (summary.portion/100)), 1)
        fatPerc100g = round((summary.fat / (summary.portion/100)), 1)
        return [protPer100g, carbPer100g, fatPerc100g]