class Meal:
    def __init__ (self, desc, cal, protein):
        self.type = 'Meal'
        self.desc = desc
        self.cal = cal
        self.protein = protein

    def __repr__(self):
        return f"[{self.type}: {self.desc}, {self.cal:.0f} calories, {self.protein:.0f}g protein]"

class Snack:
    def __init__ (self, name, servings, servCal, servProtein):
        self.type = 'Snack'
        self.name = name
        self.servings = servings
        self.servCal = servCal
        self.servPrt = servProtein
        self.cal = self.servings * self.servCal
        self.protein = self.servings * self.servPrt
    
    def __repr__(self):
        return f"[{self.type}: {self.name}, {self.servings:.0f} servings, {self.cal:.0f} calories, {self.protein:.0f}g protein]"