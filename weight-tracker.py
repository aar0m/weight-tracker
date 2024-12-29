from food import Meal
from food import Snack
import html
import os
import datetime


# Format functions ///////////

def prLine():
    size = os.get_terminal_size()
    print("\n")
    print("=" * size.columns)
    print("\n")

def getCalHead():
    prLine()
    print("Calorie Logging Initiated . . .")
    prLine()

# Logic functions ////////////
def getCal():
    getCalHead()

    mealTypes = ["Breakfast", "Lunch", "Dinner", "Snack"]

    while True: 
        print("What type of food are you logging?")
        for i, mealType in enumerate(mealTypes):
            print(f"{i+1}. {mealType}")
        break

    possVal = f"[1 - {len(mealTypes)}]"
    chosenType = int(input(f"\nWhat kind of food are you logging? Enter a value from {possVal}: ")) - 1

    try:
        print(f"\nYou are logging your {mealTypes[chosenType]}.")
    except:
        print(f"ERROR: Please enter a value from {possVal}.")

    if chosenType in range(len(mealTypes) - 1):
        mealDesc = html.escape(input("Describe your meal (what did you eat?):\n"))
        eatenCal = int(input("\nEnter the number of calories(kCal) eaten: "))
        eatenPrt = int(input("Enter the number of protein(g) in the meal: "))

        loggedFood = Meal(desc=mealDesc, cal=eatenCal, protein=eatenPrt)
        
        prLine()
        print(f"Logging {loggedFood.cal} calories and {loggedFood.protein}g protein consumed for {mealTypes[chosenType]}.")
        print(f"You ate {loggedFood.desc}!")
        prLine()

    elif chosenType + 1 == len(mealTypes):
        snackName = html.escape(input("What is the name of your snack?:\n"))
        servSize = float(input("\nEnter the number of servings eaten: "))
        eatenCal = int(input("How many calories(kCal) are in each serving?: "))
        eatenPrt = int(input("Enter the number of protein(g) in the meal: "))
        
        loggedFood = Snack(name=snackName, servings=servSize, cal=eatenCal, protein=eatenPrt)
       
        prLine()
        print(f"Logging {loggedFood.cal} calories and {loggedFood.protein}g protein consumed for a {mealTypes[chosenType]}.")
        print(f"You ate {loggedFood.servings} servings of {loggedFood.name}!")
        prLine()

    return loggedFood

def saveCal():
    # print("saveCal() running successfully")
    pass

def showCal():
    # print("showCal() running successfully")
    pass

def main():
    getCal()
    saveCal()
    showCal()

if __name__  == "__main__":
    main()
