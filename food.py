class Meal:
    def __init__ (self, date, desc, cal, protein):
        self.date = date
        self.type = 'Meal'
        self.desc = desc
        self.cal = cal
        self.protein = protein

    def __repr__(self):
        return f"[{self.date}] {self.type}:{self.desc}, {self.cal:.0f} calories, {self.protein:.0f}g protein"

class Snack:
    def __init__ (self, date, name, servings, servCal, servProtein):
        self.date = date
        self.type = 'Snack'
        self.name = name
        self.servings = servings
        self.servCal = servCal
        self.servPrt = servProtein
        self.cal = self.servings * self.servCal
        self.protein = self.servings * self.servPrt
    
    def __repr__(self):
        return f"[{self.date}] {self.type}:{self.name}, {self.servings:.0f} servings, {self.cal:.0f} calories, {self.protein:.0f}g protein"
    
class Weight:
    def __init__ (self, date, weight):
        self.date = date
        self.weight = weight
    
    def __repr__(self):
        return f"[{self.date}] {self.weight}lbs"