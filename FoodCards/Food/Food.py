class Food:
    def __init__(self, name = ""):
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
        self.kcal += other.kcal
        self.fat += other.fat
        self.fat_unsat_mono += other.fat_unsat_mono
        self.fat_unsat_bi += other.fat_unsat_bi
        self.fat_sat += other.fat_sat
        self.prot += other.prot
        self.carb += other.carb
        self.carb_sugar += other.carb_sugar
        self.fiber += other.fiber
        return self

    def __mul__(self, multi):
        self.kcal *= multi
        self.fat *= multi
        self.fat_unsat_mono *= multi
        self.fat_unsat_bi *= multi
        self.fat_sat *= multi
        self.prot *= multi
        self.carb *= multi
        self.carb_sugar *= multi
        self.fiber *= multi
        return self

    def __eq__(self, other):
        result = False
        if(other != None and
           self.kcal == other.kcal and
           self.prot == other.prot and
           self.fat == other.fat and
           self.fat_sat == other.fat_sat and
           self.fat_unsat_mono == other.fat_unsat_mono and
           self.fat_unsat_bi == other.fat_unsat_bi and
           self.carb == other.carb and
           self.carb_sugar == other.carb_sugar and
           self.fiber == other.fiber):
            result = True
        return result

    def addPortion(self, other):
        self.__add__(other.scalePortion())
        self.portion += other.portion

    def getFoodNutricion(self):
        entirePortion = self.scalePortion()
        return [self.name,
                self.portion,
                entirePortion.kcal,
                entirePortion.prot,
                entirePortion.fat,
                entirePortion.fat_sat,
                entirePortion.fat_unsat_mono,
                entirePortion.fat_unsat_bi,
                entirePortion.carb,
                entirePortion.carb_sugar,
                entirePortion.fiber]

    def getFoodNutricionPer100g(self):
        return [self.name,
                100,
                self.kcal,
                self.prot,
                self.fat,
                self.fat_sat,
                self.fat_unsat_mono,
                self.fat_unsat_bi,
                self.carb,
                self.carb_sugar,
                self.fiber]

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