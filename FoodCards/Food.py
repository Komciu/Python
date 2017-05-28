class Food:
    def __init__(self, name):
        self.name = name
        self.kcal = 0
        self.fat = 0
        self.fat_unsat_mono = 0
        self.fat_unsat_bi = 0
        self.fat_sat = 0
        self.prot = 0
        self.carb = 0
        self.carb_sugar = 0
        self.fiber = 0
        self.portion = 100

    def __add__(self, other):
        otherPortion = other.scalePortion()
        self.kcal += otherPortion.kcal
        self.fat += otherPortion.fat
        self.fat_unsat_mono += otherPortion.fat_unsat_mono
        self.fat_unsat_bi += otherPortion.fat_unsat_bi
        self.fat_sat += otherPortion.fat_sat
        self.prot += otherPortion.prot
        self.carb += otherPortion.carb
        self.carb_sugar += otherPortion.carb_sugar
        self.fiber += otherPortion.fiber
        return self

    def getName(self):
        return self.name

    def getFoodNutricion(self):
        entirePortion = self.scalePortion()
        return [self.name,
                self.portion,
                entirePortion.kcal,
                entirePortion.fat,
                entirePortion.fat_unsat_mono,
                entirePortion.fat_unsat_bi,
                entirePortion.fat_sat,
                entirePortion.prot,
                entirePortion.carb,
                entirePortion.carb_sugar,
                entirePortion.fiber]

    def scalePortion(self):
        entirePortion = Food(self.name)
        entirePortion.kcal = self.kcal * self.portion/100
        entirePortion.fat = self.fat * self.portion/100
        entirePortion.fat_unsat_mono = self.fat_unsat_mono * self.portion/100
        entirePortion.fat_unsat_bi = self.fat_unsat_bi * self.portion/100
        entirePortion.fat_sat = self.fat_sat * self.portion/100
        entirePortion.prot = self.prot * self.portion/100
        entirePortion.carb = self.carb * self.portion/100
        entirePortion.carb_sugar = self.carb_sugar * self.portion/100
        entirePortion.fiber = self.fiber * self.portion/100
        return entirePortion