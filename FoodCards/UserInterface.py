from Meal.Meal import Meal
from Food.Food import Food
from FoodDB.FoodFileSystem import FoodFileSystem

class UI:
    def __init__(self):
        pass

    def start(self):
        meal = self.createMeal()
        self.fdb = FoodFileSystem("Data/nutricion.csv")
        meal.addFood(self.createIngridient())
        while(input("Starczy?") != ('tak' or 't')):
            meal.addFood(self.createIngridient())
        self.fdb.saveToFile(meal)

    def createMeal(self):
        name = input("Podaj nazwe posilku: ")
        meal = Meal(name)
        return meal

    def createIngridient(self):
        name = input("Podaj nazwe skladnika: ")
        ingr = Food(name)
        portion = int(input("Podaj rozmiar porcji: "))
        ingr.portion = portion
        if(self.fdb.isPresent(name)):
            ingr = self.fdb.findFood(name)
            ingr.portion = portion
        else:
            kcal = self.safeFloatInput("Podaj ilosc kilokalorii: ")
            ingr.kcal = kcal
            fat = self.safeFloatInput("Podaj ilosc tluszczow: ")
            ingr.fat = fat
            fatS = self.safeFloatInput("Podaj ilosc tluszczow nasyconych: ")
            ingr.fat_sat = fatS
            fatUsM = self.safeFloatInput("Podaj ilosc tluszczow nienasyconych mono: ")
            ingr.fat_unsat_mono = fatUsM
            fatUsB = self.safeFloatInput("Podaj ilosc tluszczow nienasyconych bi: ")
            ingr.fat_unsat_bi = fatUsB
            prot = self.safeFloatInput("Podaj ilosc  bialka: ")
            ingr.prot = prot
            carb = self.safeFloatInput("Podaj ilosc  weglowodanow: ")
            ingr.carb = carb
            carbS = self.safeFloatInput("Podaj ilosc  cukrow: ")
            ingr.carb_sugar = carbS
            fiber = self.safeFloatInput("Podaj ilosc blonnika: ")
            ingr.fiber = fiber
            self.fdb.addFood(ingr)
        return ingr

    def safeFloatInput(self, txt):
        value = input(txt)
        if(value == ''):
            value = 0
        else:
            value = float(value)
        return value