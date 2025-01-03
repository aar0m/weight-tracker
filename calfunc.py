"""
///                        -------------------------
///                              Weight Tracker
///                        -------------------------
///                           By Aaron Ramos 2025
///
/// All logic functions required to log, view, and handle calorie- and protein-
/// related items.
///
/// @file calfunc.py
/// @author Aaron Ramos (ramosaaron2@gmail.com)
///
"""

from food import Meal
from food import Snack
from datetime import datetime
import html
import os
import datetime
import format as fr

size = fr.size

def getCal():
    fr.prMethodHead("Calorie Logging Process Initiated")
    mealTypes = ["Breakfast", "Lunch", "Dinner", "Snack"]

    while True: 
        print("What type of food are you logging?")
        for i, mealType in enumerate(mealTypes):
            print(f"{i+1}. {mealType}")
        break

    possVal = f"[1 - {len(mealTypes)}]"
    
    try:
        chosenType = int(input(f"\nEnter a value from {possVal}: ")) - 1
    except ValueError:
        fr.prErrorMes(f"Please enter a value from {possVal}.")
        exit
    except IndexError:
        fr.prErrorMes(f"Please enter a value from {possVal}.")
        exit
    except UnboundLocalError:
        fr.prErrorMes(f"Please enter a value from {possVal}.")
        exit

    print(f"\nYou are logging a {mealTypes[chosenType]}.")

    if chosenType in range(len(mealTypes) - 1): # For Meals
        mealDesc = html.escape(input("Describe your meal (what did you eat?):\n"))
        mealDesc = mealDesc.translate(str.maketrans('', '', '@#$%^*;'))
        eatenCal = int(input("\nEnter the number of calories(kCal) eaten: "))
        eatenPrt = int(input("Enter the number of protein(g) in the meal: "))

        loggedFood = Meal(date=datetime.date.today(), desc=mealDesc, cal=eatenCal, protein=eatenPrt)
        
        fr.prLine()
        print(f"Logging {loggedFood.cal} calories and {loggedFood.protein}g protein from {mealTypes[chosenType]}.".center(size.columns))
        print(f"You ate {loggedFood.desc}!".center(size.columns))
        fr.prLine()

    elif chosenType + 1 == len(mealTypes): # For Snacks
        snackName = html.escape(input("What is the name of your snack?: "))
        snackName = snackName.translate(str.maketrans('', '', '@#$%^*;'))
        servSize  = float(input("\nEnter the number of servings eaten: "))
        servCals  = int(input("How many calories(kCal) are in each serving?: "))
        servPrt  = int(input("Enter the number of protein(g) in each serving: "))

        loggedFood = Snack(date=datetime.date.today(), name=snackName, servings=servSize, servCal=servCals, servProtein=servPrt)
       
        fr.prLine()
        print(f"Logging {loggedFood.cal:.0f} calories and {loggedFood.protein:.0f}g protein from a {mealTypes[chosenType]}.".center(size.columns))
        print(f"You ate {loggedFood.servings:.0f} servings of {loggedFood.name}!".center(size.columns))
        fr.prLine()

    return loggedFood

def save(food, cal_file_path):
    fr.prMethodHead(f"Recorded {food} to {str(cal_file_path).split('/')[3]}!")

    with open(cal_file_path, "a") as f:
        if isinstance(food, Meal):
            f.write(f"{datetime.date.today()}; M; {food.desc};{food.cal};{food.protein}\n")

        elif isinstance(food, Snack):
            f.write(f"{datetime.date.today()}; S; {food.name};{food.servings};{food.cal};{food.protein}\n")
    f.close()

def calInterface(cal_file_path):
    fr.prMethodHead("Displaying Logged Calories")

    options = ["Today", "Week", "Month", "Return to Main Menu"]

    print("Which calorie(s) would you like to view?")
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")
    
    possVal = f"[1 - {len(options)}]"
    
    try:
        chosenOpt = int(input(f"\nEnter a value from {possVal}: ")) - 1
    except ValueError:
        chosenOpt = 99999
    
    match chosenOpt:
        case 0:
            summToday(cal_file_path)
        case 1:
            summWeek()
        case 2:
            summMonth()
        case 3:
            print("Returning to Main Menu".center(32, "-"), "\n")
            exit
        case _:
            fr.prErrorMes(f"Invalid input. Please enter a value from {possVal}.")

def readList(cal_file_path):
    foodCal = []

    with open(cal_file_path, "r") as f:
        lines = f.readlines()

        if len(lines) == 0:
            fr.prErrorMes("You have not logged any calories!")
            exit

        for line in lines:
            if line[12] == 'M':
                calDate, calType, mealDesc, mealCal, mealPrt = line.strip().split(";")
                line_cal = Meal(date=calDate, desc=mealDesc, cal=int(mealCal), protein=int(mealPrt))

            elif line[12] == 'S':
                calDate, calType, snackName, snackServ, snackCal, snackPrt = line.strip().split(";")
                line_cal = Snack(
                    date        = calDate,
                    name        = snackName, 
                    servings    = float(snackServ), 
                    servCal     = (float(snackCal) / float(snackServ)), 
                    servProtein = (float(snackPrt) / float(snackServ)))
            
            foodCal.append(line_cal)
    f.close()
    
    return foodCal

def summFood(cal_dir_path):
    fr.prMethodHead(f"Displaying {datetime.date.today().strftime('%Y')} Food Log")
    for file in os.listdir(cal_dir_path):
        cal_file_path = f"tracker-sheets/calorie/calories{datetime.date.today().strftime('%Y')}/{file}"
        foodList = readList(cal_file_path)

        print(f"- {datetime.datetime.strptime(foodList[0].date, '%Y-%m-%d').date().strftime('%B')} -".center(size.columns))
        for food in foodList:
            print(f"{food}".center(size.columns).ljust(size.columns))
        print("\n")
    fr.prLine()

def summToday(cal_file_path):
    fr.prMethodHead("Displaying Calories and Protein Consumed Today")
    foodList = readList(cal_file_path)

    if os.path.getsize(cal_file_path) == 0:
        return 0

    for food in foodList:
        if str(food.date) == datetime.date.today().strftime('%Y-%m-%d'):
            print(f"{food}".center(size.columns).ljust(size.columns))

    dailyCal = {}
    for food in foodList:
        key = food.date
        if key in dailyCal:
            dailyCal[key] = [dailyCal[key][0] + food.cal, dailyCal[key][1] + food.protein]
        else:
            dailyCal[key] = [food.cal, food.protein]
    
    keyList = list(dailyCal.keys())
    for key in keyList:
        if str(key) == datetime.date.today().strftime('%Y-%m-%d'):
            print("\n" + f"Total: {dailyCal[key][0]} calories, {dailyCal[key][1]}g protein".center(size.columns))
    fr.prLine()

def summWeek():
    fr.prMethodHead("Displaying Calories and Protein Consumed in the Past Week")
    file = f"calories{datetime.date.today().strftime('_%m-%Y')}.csv"
    cal_file_path = f"tracker-sheets/calorie/calories{datetime.date.today().strftime('%Y')}/{file}"
    foodList = readList(cal_file_path)
    avgCal, avgPrt = 0, 0

    if os.path.getsize(cal_file_path) == 0:
        return 0

    dailyCal = {}
    for food in foodList:
        key = food.date
        if key in dailyCal:
            dailyCal[key] = [dailyCal[key][0] + food.cal, dailyCal[key][1] + food.protein]
        else:
            dailyCal[key] = [food.cal, food.protein]
    
    keyList = list(dailyCal.keys())
    if len(keyList) < 7:
        for key in keyList:
            print(f"[{key}] {dailyCal[key][0]} calories, {dailyCal[key][1]}g protein".center(size.columns))
            avgCal += int(dailyCal[key][0])
            avgPrt += int(dailyCal[key][1])
    else:
        for key in keyList[len(keyList)-7:len(keyList)]:
            print(f"[{key}] {dailyCal[key][0]} calories, {dailyCal[key][1]}g protein".center(size.columns))
            avgCal += int(dailyCal[key][0])
            avgPrt += int(dailyCal[key][1])

    print("\n" + f"Total: {avgCal} calories, {avgPrt}g protein".center(size.columns))

    if len(keyList) < 7:
        avgCal /= len(keyList)
        avgPrt /= len(keyList)
    else:
        avgCal /= 7
        avgPrt /= 7

    print(f"Average: {avgCal:.1f} calories, {avgPrt:.1f}g protein".center(size.columns))
    fr.prLine()
    
def summMonth():
    fr.prMethodHead(f"Displaying Calories and Protein Consumed in {datetime.date.today().strftime('%B')}")
    file = f"calories{datetime.date.today().strftime('_%m-%Y')}.csv"
    cal_file_path = f"tracker-sheets/calorie/calories{datetime.date.today().strftime('%Y')}/{file}"
    foodList = readList(cal_file_path)
    avgCal, avgPrt = 0, 0

    if os.path.getsize(cal_file_path) == 0:
        return 0

    dailyCal = {}
    for food in foodList:
        key = food.date
        if key in dailyCal:
            dailyCal[key] = [dailyCal[key][0] + food.cal, dailyCal[key][1] + food.protein]
        else:
            dailyCal[key] = [food.cal, food.protein]

    for day, food in dailyCal.items():
        print(f"[{day}] {food[0]} calories, {food[1]}g protein".center(size.columns))
        avgCal += int(food[0])
        avgPrt += int(food[1])
    
    print("\n" + f"Total: {avgCal} calories, {avgPrt}g protein".center(size.columns))
    
    avgCal /= len(dailyCal.items())
    avgPrt /= len(dailyCal.items())
    
    print(f"Average: {avgCal:.1f} calories, {avgPrt:.1f}g protein".center(size.columns))
    fr.prLine()
