from food import Meal
from food import Snack
import html
import os
import datetime


# Format functions ///////////
size = os.get_terminal_size()

def prLine():
    print("\n")
    print("=" * size.columns)
    print("\n")

def prLineThin():
    print("\n")
    print("-" * size.columns)
    print("\n")

def prProgHead():
    size = os.get_terminal_size()

    prLine()
    print("Weight Tracker 0.0.0".center(size.columns))
    print("A Python program to track your calories, protein intake, and weight.".center(size.columns))
    print("-----------------------------------------------".center(size.columns))
    print("Created by Aaron Ramos (ramosaaron2@gmail.com)".center(size.columns))
    print("Based on 'Expense Tracking App' Project by pixegami".center(size.columns))
    prLine()

def prCalHead():
    prLine()
    print("Calorie Logging Process Initiated".center(size.columns))
    prLine()

def prSummHead():
    prLine()
    print(f"Summarizing Calories Consumed".center(size.columns))
    prLineThin()

def prDetailHead():
    prLine()
    print(f"Providing Caloric Breakdown and Protein Consumed".center(size.columns))
    prLineThin()

# Logic functions ////////////

def getCal():
    prCalHead()
    mealTypes = ["Breakfast", "Lunch", "Dinner", "Snack"]

    while True: 
        print("What type of food are you logging?")
        for i, mealType in enumerate(mealTypes):
            print(f"{i+1}. {mealType}")
        break

    possVal = f"[1 - {len(mealTypes)}]"
    chosenType = int(input(f"\nEnter a value from {possVal}: ")) - 1

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
        print(f"Logging {loggedFood.cal} calories and {loggedFood.protein}g protein consumed for {mealTypes[chosenType]}.".center(size.columns))
        print(f"You ate {loggedFood.desc}!".center(size.columns))
        prLine()

    elif chosenType + 1 == len(mealTypes): # For Snacks
        snackName = html.escape(input("What is the name of your snack?: "))
        servSize  = float(input("\nEnter the number of servings eaten: "))
        servCals  = int(input("How many calories(kCal) are in each serving?: "))
        servPrt  = int(input("Enter the number of protein(g) in each serving: "))

        loggedFood = Snack(name=snackName, servings=servSize, servCal=servCals, servProtein=servPrt)
       
        prLine()
        print(f"Logging {loggedFood.cal:.0f} calories and {loggedFood.protein:.0f}g protein consumed for a {mealTypes[chosenType]}.".center(size.columns))
        print(f"You ate {loggedFood.servings:.0f} servings of {loggedFood.name}!".center(size.columns))
        prLine()

    return loggedFood

def saveCal(food, cal_file_path):
    print(f"Recorded {food} to {cal_file_path}!")
    prLine()
    
    with open(cal_file_path, "a") as f:
        if isinstance(food, Meal):
            f.write(f"M, {food.desc},{food.cal},{food.protein}\n")

        elif isinstance(food, Snack):
            f.write(f"S, {food.name},{food.servings},{food.cal},{food.protein}\n")

def readList(cal_file_path):
    foodCal = []

    with open(cal_file_path, "r") as f:
        lines = f.readlines()

        for line in lines:
            if line[0] == 'M':
                calType, mealDesc, mealCal, mealPrt = line.strip().split(",")
                line_cal = Meal(desc=mealDesc, cal=int(mealCal), protein=int(mealPrt))

            elif line[0] == 'S':
                calType, snackName, snackServ, snackCal, snackPrt = line.strip().split(",")
                line_cal = Snack(
                    name        = snackName, 
                    servings    = float(snackServ), 
                    servCal     = (float(snackCal) / float(snackServ)), 
                    servProtein = (float(snackPrt) / float(snackServ)))
            
            foodCal.append(line_cal)
    
    return foodCal

def summCal(cal_file_path):
    prSummHead()
    foodCal = readList(cal_file_path)

    print("Food Eaten".center(32, "-").center(size.columns))
    for food in foodCal:
        print(f"{food}".center(size.columns).ljust(size.columns))
    prLine()

def summDetails(cal_file_path):
    prDetailHead()
    foodCal = readList(cal_file_path)

    calByType = {}
    for food in foodCal:
        key = food.type
        if key in calByType:
            calByType[key] += food.cal
        else:
            calByType[key] = food.cal


    prtByType = {}
    for food in foodCal:
        key = food.type
        if key in prtByType:
            prtByType[key] += food.protein
        else:
            prtByType[key] = food.protein

    print("Calorie Breakdown:".center(32, "-").center(size.columns))
    for typeCal, amount in calByType.items():
        print(f"{typeCal}s: {amount} calories".center(size.columns))
    prLineThin()

    print("Protein Breakdown:".center(32, "-").center(size.columns))
    for typeCal, amount in prtByType.items():
        print(f"{typeCal}s: {amount}g protein".center(size.columns))
    prLine()

def main():
    prProgHead()
    #TODO: Weight input using datetime
    #TODO: Average weight/week/month (good luck lol)

    cal_file_path = "calorie.csv"
    
    options = ["Log Calories", "Show Food Log", "Calorie/Protein Breakdown", "Exit"]

    while True: 
        print("\nWelcome! What would you like to do today?")
        for i, option in enumerate(options):
            print(f"{i+1}. {option}")
        
        possVal = f"[1 - {len(options)}]"
        chosenOpt = int(input(f"\nEnter a value from {possVal}: ")) - 1
        
        match chosenOpt:
            case 0:
                food = getCal()
                saveCal(food, cal_file_path)
            case 1:
                summCal(cal_file_path)
            case 2:
                summDetails(cal_file_path)
            case 3:
                print("Exiting Now".center(32, "-"), "\n")
                break

if __name__  == "__main__":
    main()
