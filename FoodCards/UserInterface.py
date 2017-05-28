from Meal import Meal
from Food import Food


class UI:
    def __init__(self):
        pass

    def start(self):
        meal = self.createMeal()
        while(input("Starczy?") != 'tak'):
            meal.addFood(self.createIngridient())
        meal.saveToFile()

    def createMeal(self):
        name = input("Podaj nazwe posilku: ")
        meal = Meal(name)
        return meal

    def createIngridient(self):
        name = input("Podaj nazwe skladnika: ")
        ingr = Food(name)
        portion = int(input("Podaj rozmiar porcji: "))
        ingr.portion = portion
        kcal = int(input("Podaj ilosc kilokalorii: "))
        ingr.kcal = kcal
        fat = int(input("Podaj ilosc tluszczow: "))
        ingr.fat = fat
        fatS = int(input("Podaj ilosc tluszczow nasyconych: "))
        ingr.fat_sat = fatS
        fatUsM = int(input("Podaj ilosc tluszczow nienasyconych mono: "))
        ingr.fat_unsat_mono = fatUsM
        fatUsB = int(input("Podaj ilosc tluszczow nienasyconych bi: "))
        ingr.fat_unsat_bi = fatUsB
        prot = int(input("Podaj ilosc  bialka: "))
        ingr.prot = prot
        carb = int(input("Podaj ilosc  weglowodanow: "))
        ingr.carb = carb
        carbS = int(input("Podaj ilosc  cukrow: "))
        ingr.carb_sugar = carbS
        fiber = int(input("Podaj ilosc blonnika: "))
        ingr.fiber = fiber
        return ingr