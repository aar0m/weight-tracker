from food import Meal
from food import Snack
from food import Weight
from datetime import datetime
import html
import os
import datetime

# Format functions ///////////
size = os.get_terminal_size()

def prLine():
    print("\n" + "=" * size.columns + "\n")

def prProgHead():
    size = os.get_terminal_size()

    prLine()
    print("Weight Tracker 1.1.0".center(size.columns))
    print("A Python program to track your calories, protein intake, and weight.".center(size.columns))
    print("-----------------------------------------------".center(size.columns))
    print("Created by Aaron Ramos (ramosaaron2@gmail.com)".center(size.columns))
    print("Based on 'Expense Tracking App' Project by pixegami".center(size.columns))
    prLine()

def prMethodHead(text):
    prLine()
    print(f"{text}".center(size.columns))
    print("\n" + "=" * size.columns + "\n")

def prErrorMes(text):
    print("\n" + ("x" * int(size.columns/2)).center(size.columns) + "\n")
    print(f"{text}".center(size.columns))
    print("\n" + ("x" * int(size.columns/2)).center(size.columns) + "\n")

# Logic functions ////////////

def getCal():
    prMethodHead("Calorie Logging Process Initiated")
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
        prErrorMes(f"ERROR: Please enter a value from {possVal}.")
        exit

    print(f"\nYou are logging a {mealTypes[chosenType]}.")

    if chosenType in range(len(mealTypes) - 1): # For Meals
        mealDesc = html.escape(input("Describe your meal (what did you eat?):\n"))
        eatenCal = int(input("\nEnter the number of calories(kCal) eaten: "))
        eatenPrt = int(input("Enter the number of protein(g) in the meal: "))

        loggedFood = Meal(date=datetime.date.today(), desc=mealDesc, cal=eatenCal, protein=eatenPrt)
        
        prMethodHead(f"Logging {loggedFood.cal} calories and {loggedFood.protein}g protein consumed for {mealTypes[chosenType]}. You ate {loggedFood.desc}!")

    elif chosenType + 1 == len(mealTypes): # For Snacks
        snackName = html.escape(input("What is the name of your snack?: "))
        servSize  = float(input("\nEnter the number of servings eaten: "))
        servCals  = int(input("How many calories(kCal) are in each serving?: "))
        servPrt  = int(input("Enter the number of protein(g) in each serving: "))

        loggedFood = Snack(date=datetime.date.today(), name=snackName, servings=servSize, servCal=servCals, servProtein=servPrt)
       
        prLine()
        print(f"Logging {loggedFood.cal:.0f} calories and {loggedFood.protein:.0f}g protein consumed for a {mealTypes[chosenType]}.".center(size.columns))
        print(f"You ate {loggedFood.servings:.0f} servings of {loggedFood.name}!".center(size.columns))
        prLine()

    return loggedFood

def saveCal(food, cal_file_path):
    prMethodHead(f"Recorded {food} to {cal_file_path}!")
    
    with open(cal_file_path, "a") as f:
        if isinstance(food, Meal):
            f.write(f"{datetime.date.today()}, M, {food.desc},{food.cal},{food.protein}\n")

        elif isinstance(food, Snack):
            f.write(f"{datetime.date.today()}, S, {food.name},{food.servings},{food.cal},{food.protein}\n")
    f.close()

def readCalList(cal_file_path):
    foodCal = []

    with open(cal_file_path, "r") as f:
        lines = f.readlines()

        for line in lines:
            if line[12] == 'M':
                calDate, calType, mealDesc, mealCal, mealPrt = line.strip().split(",")
                line_cal = Meal(date=calDate, desc=mealDesc, cal=int(mealCal), protein=int(mealPrt))

            elif line[12] == 'S':
                calDate, calType, snackName, snackServ, snackCal, snackPrt = line.strip().split(",")
                line_cal = Snack(
                    date        = calDate,
                    name        = snackName, 
                    servings    = float(snackServ), 
                    servCal     = (float(snackCal) / float(snackServ)), 
                    servProtein = (float(snackPrt) / float(snackServ)))
            
            foodCal.append(line_cal)
    f.close()
    
    return foodCal

def summCal(cal_file_path):
    prMethodHead("Summarizing Calories Consumed")
    foodCal = readCalList(cal_file_path)

    for food in foodCal:
        print(f"{food}".center(size.columns).ljust(size.columns))
    prLine()

def summCalDetails(cal_file_path):
    prMethodHead("Providing Daily Intake of Calories and Protein")
    foodCal = readCalList(cal_file_path)

    dailyCal = {}
    for food in foodCal:
        key = food.date
        if key in dailyCal:
            dailyCal[key] = [dailyCal[key][0] + food.cal, dailyCal[key][1] + food.protein]
        else:
            dailyCal[key] = [food.cal, food.protein]

    for day, food in dailyCal.items():
        print(f"[{day}] {food[0]} calories, {food[1]}g protein".center(size.columns))
    prLine()

def getWeight():
    prMethodHead("Weight Logging Process Initiated")

    try:
        weight = float(input("Please enter your measured weight (lbs): "))

    except ValueError:
        prErrorMes("ERROR: Only enter the number of your measured weight (lbs).")
        exit
    
    return weight

def saveWeight(weight, weight_file_path):
    prMethodHead(f"Recorded {weight}lbs to {weight_file_path}!")
    
    try:
        with open(weight_file_path, "r+") as f:
            lines = f.readlines()
            lineDate = lines[-1].split(",")[0]
            # DEBUG: print(f"{lines[len(lines)-1].split(",")[0] == str(datetime.date.today())}")

            if lineDate == str(datetime.date.today()):
                lines[-1] = f"{datetime.date.today()}, {weight}\n"
                
                with open(weight_file_path, "w") as f:
                    f.writelines(lines)
            else:
                with open(weight_file_path, "a") as f:
                    f.write(f"{datetime.date.today()}, {weight}\n")
        f.close()

    except FileNotFoundError:
        with open(weight_file_path, "a") as f:
            f.write(f"{datetime.date.today()}, {weight}\n")
        f.close()

def weightInterface(weight_file_path):
    prMethodHead("Summarizing Logged Weight")

    options = ["Today", "Week (7 Days)", "Month", "Year", "Return to Main Menu"]

    print("Which weight(s) would you like to view?")
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")
    
    possVal = f"[1 - {len(options)}]"
    
    try:
        chosenOpt = int(input(f"\nEnter a value from {possVal}: ")) - 1
    except ValueError:
        chosenOpt = 99999
    
    match chosenOpt:
        case 0:
            summWeightToday(weight_file_path)
        case 1:
            summWeightWeek(weight_file_path)
        case 2:
            pass #TODO: add monthly using key check
        case 3:
            pass #TODO: add yearly using key check
        case 4:
            print("Returning to Main Menu".center(32, "-"), "\n")
            exit
        case _:
            prErrorMes(f"ERROR: Invalid input. Please enter a value from {possVal}.")

def readWeightList(weight_file_path):
    weightList = []

    with open(weight_file_path, "r") as f:
        lines = f.readlines()
        
        for line in lines:
            weightDate, weightNum = line.strip().split(",")
            line_weight = Weight(date=weightDate, weight=weightNum)

            weightList.append(line_weight)
    f.close

    return weightList

def summWeightToday(weight_file_path):
    wList = readWeightList(weight_file_path)

    if wList[-1].date == str(datetime.date.today()):
        prMethodHead(f"Your weight as of {datetime.date.today().strftime("%A, %B %d %Y")} is{wList[-1].weight}lbs.")
    else:
        prLine()
        print("You have not logged your weight today!".center(size.columns))
        print(f"Your weight as of {datetime.datetime.strptime(wList[-1].date, '%Y-%m-%d').date().strftime("%A, %B %d %Y")} is{wList[-1].weight}lbs.".center(size.columns))
        prLine()

def summWeightWeek(weight_file_path):
    prMethodHead("Calculating Average Weight Over the Past Week")
    wList = readWeightList(weight_file_path)
    avgWeight = 0

    if len(wList) < 7:
        for weight in wList:
            print(f"{weight}".center(size.columns))
            avgWeight += float(weight.weight)
        
        avgWeight = avgWeight / len(wList)
    else:
        for weight in wList[len(wList)-7:len(wList)]:
            print(f"{weight}".center(size.columns))
            avgWeight += float(weight.weight)

        avgWeight = avgWeight / 7

    print("\n" + f"Your average weight over the past week is {avgWeight:.2f}lbs.".center(size.columns))
    prLine()

def summWeightMonth(weight_file_path):
    prMethodHead(f"Calculating Average Weight Over {datetime.date.today().strftime("%B")}")
    wList = readWeightList(weight_file_path)
    avgWeight = 0
    
    wListMonth = []
    for weight in wList:
        todayMonth = datetime.date.today().strftime("%B")
        wEntryMonth = datetime.datetime.strptime(weight.date, '%Y-%m-%d').date().strftime("%B")
        
        if todayMonth == wEntryMonth:
            wListMonth.append(weight)
    
    for wEntry in wListMonth:
        print(f"{wEntry}".center(size.columns))
        avgWeight += float(wEntry.weight)
    
    avgWeight = avgWeight / len(wListMonth)

    print("\n" + f"Your average weight over {datetime.date.today().strftime("%B")} is {avgWeight:.2f}lbs.".center(size.columns))
    prLine()


def main():
    prProgHead()
    #TODO: Average weight/week/month (good luck lol)

    cal_file_path = f"calorie-sheets/calorie{datetime.date.today().strftime("%Y")}.csv"
    weight_file_path = f"weight-sheets/weight{datetime.date.today().strftime("%Y")}.csv"
    
    options = ["Log Calories", "Log Weight", f"View {datetime.date.today().strftime("%Y")} Food Log", "View Daily Calories/Protein", "View Weight", "Exit"]

    while True: 
        print("Welcome! What would you like to do today?")
        for i, option in enumerate(options):
            print(f"{i+1}. {option}")
        
        possVal = f"[1 - {len(options)}]"
        
        try:
            chosenOpt = int(input(f"\nEnter a value from {possVal}: ")) - 1
        except ValueError:
            chosenOpt = 99999
        
        match chosenOpt:
            case 0:
                food = getCal()
                saveCal(food, cal_file_path)
            case 1:
                weight = getWeight()
                saveWeight(weight, weight_file_path)
            case 2:
                try:
                    summCal(cal_file_path)
                except FileNotFoundError:
                    prErrorMes(f"ERROR: You have not logged any calories for {datetime.date.today().strftime("%Y")}!")
                    exit
            case 3:
                try:
                    summCalDetails(cal_file_path)
                except FileNotFoundError:
                    prErrorMes(f"ERROR: You have not logged any calories for {datetime.date.today().strftime("%Y")}!")
                    exit
            case 4:
                summWeightMonth(weight_file_path)
                # weightInterface(weight_file_path)
            case 5:
                print("Exiting Now".center(32, "-"), "\n")
                break
            case _:
                prErrorMes(f"ERROR: Invalid input. Please enter a value from {possVal}.")

if __name__  == "__main__":
    main()
