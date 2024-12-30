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
    print("Calorie Logging Process Initiated . . . ")
    prLine()

# Logic functions ////////////
def getCal():
    mealTypes = ["Breakfast", "Lunch", "Dinner", "Snack"]

    while True: 
        print("What type of food are you logging?")
        for i, mealType in enumerate(mealTypes):
            print(f"{i+1}. {mealType}")
        break

    possVal = f"[1 - {len(mealTypes)}]"
    chosenType = int(input(f"\nWhat kind of food are you logging? Enter a value from {possVal}: ")) - 1

    try:
        print(f"\nYou are logging a {mealTypes[chosenType]}.")
    except:
        print(f"ERROR: Please enter a value from {possVal}.")
        exit

    if chosenType in range(len(mealTypes) - 1): # For Meals
        mealDesc = html.escape(input("Describe your meal (what did you eat?):\n"))
        eatenCal = int(input("\nEnter the number of calories(kCal) eaten: "))
        eatenPrt = int(input("Enter the number of protein(g) in the meal: "))

        loggedFood = Meal(desc=mealDesc, cal=eatenCal, protein=eatenPrt)
        
        prLine()
        print(f"Logging {loggedFood.cal} calories and {loggedFood.protein}g protein consumed for {mealTypes[chosenType]}.")
        print(f"You ate {loggedFood.desc}!")
        prLine()

    elif chosenType + 1 == len(mealTypes): # For Snacks
        snackName = html.escape(input("What is the name of your snack?:\n"))
        servSize  = float(input("\nEnter the number of servings eaten: "))
        servCals  = int(input("How many calories(kCal) are in each serving?: "))
        servPrt  = int(input("Enter the number of protein(g) in each serving: "))

        loggedFood = Snack(name=snackName, servings=servSize, servCal=servCals, servProtein=servPrt)
       
        prLine()
        print(f"Logging {loggedFood.cal:.0f} calories and {loggedFood.protein:.0f}g protein consumed for a {mealTypes[chosenType]}.")
        print(f"You ate {loggedFood.servings:.0f} servings of {loggedFood.name}!")
        prLine()

    return loggedFood

def saveCal(food, cal_file_path):
    print("Logging Calories Eaten . . .")
    print(f"Recorded {food} to {cal_file_path}!")
    prLine()
    
    with open(cal_file_path, "a") as f:
        if isinstance(food, Meal):
            f.write(f"{food.desc},{food.cal},{food.protein}\n")

        elif isinstance(food, Snack):
            f.write(f"{food.name},{food.servings},{food.cal},{food.protein}\n")
    pass

def summCal(cal_file_path):
    # print("summCal() running successfully")
    pass

def main():
    # Introductory graphic
    # Match case statement

    cal_file_path = "calorie.csv"

    getCalHead()
    food = getCal()
    
    saveCal(food, cal_file_path)
    
    summCal(cal_file_path)

if __name__  == "__main__":
    main()
