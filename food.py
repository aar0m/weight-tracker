class Meal:
    def __init__ (self, desc, cal, protein):
        self.desc = desc
        self.cal = cal
        self.protein = protein

    def __repr__(self):
        return f"Meal: {self.desc}, {self.cal:.0f}, {self.protein:.0f}"

class Snack:
    def __init__ (self, name, servings, servCal, servProtein):
        self.name = name
        self.servings = servings
        self.servCal = servCal
        self.servPrt = servProtein
        self.cal = self.servings * self.servCal
        self.protein = self.servings * self.servPrt
    
    def __repr__(self):
        return f"Snack: {self.name}, {self.servings:.0f}, {self.cal:.0f}, {self.protein:.0f}"