"""
///                        -------------------------
///                              Weight Tracker
///                        -------------------------
///                           By Aaron Ramos 2025
///
/// All logic functions required to log, view, and handle weight-related items.
/// 
///
/// @file weightfunc.py
/// @author Aaron Ramos (ramosaaron2@gmail.com)
///
"""

from food import Weight
from datetime import datetime
import datetime
import os
import format as fr

size = fr.size

def getWeight():
    fr.prMethodHead("Weight Logging Process Initiated")

    try:
        weight = float(input("Please enter your measured weight (lbs): "))

    except ValueError:
        fr.prErrorMes("Only enter the number of your measured weight (lbs).")
        exit
    
    return weight

def save(weight, weight_file_path):
    fr.prMethodHead(f"Recorded {weight}lbs to {str(weight_file_path).split('/')[2]}!")

    try:
        with open(weight_file_path, "r+") as f:
            lines = f.readlines()

            if lines[-1].split(",")[0] == str(datetime.date.today()):
                lines[-1] = f"{datetime.date.today()}, {weight}\n"
                
                with open(weight_file_path, "w") as f:
                    f.writelines(lines)
                    f.close()
            else:
                with open(weight_file_path, "a") as f:
                    f.write(f"{datetime.date.today()}, {weight}\n")
                    f.close()

    except FileNotFoundError:
        with open(weight_file_path, "a") as f:
            f.write(f"{datetime.date.today()}, {weight}\n")
            f.close()

def weightInterface(weight_file_path):
    fr.prMethodHead("Summarizing Logged Weight")

    options = ["Today", "Week", "Month", "Year", f"View {datetime.date.today().strftime('%Y')} Weight Log", "Return to Main Menu"]

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
            summToday(weight_file_path)
        case 1:
            summWeek(weight_file_path)
        case 2:
            summMonth(weight_file_path)
        case 3:
            summYear(weight_file_path)
        case 4:
            summCalendar(weight_file_path)
        case 5:
            print("Returning to Main Menu".center(32, "-"), "\n")
            exit
        case _:
            fr.prErrorMes(f"Invalid input. Please enter a value from {possVal}.")

def readList(weight_file_path):
    weightList = []

    with open(weight_file_path, "r") as f:
        lines = f.readlines()

        if len(lines) == 0:
            fr.prErrorMes("You have not logged any calories!")
            exit
        
        for line in lines:
            weightDate, weightNum = line.strip().split(",")
            line_weight = Weight(date=weightDate, weight=weightNum)

            weightList.append(line_weight)
    f.close

    return weightList

def summToday(weight_file_path):
    fr.prMethodHead("Calculating Average Weight Over the Past Week")
    wList = readList(weight_file_path)

    if os.path.getsize(weight_file_path) == 0:
        return 0

    if wList[-1].date == str(datetime.date.today()):
        fr.prMethodHead(f"Your weight as of {datetime.date.today().strftime('%A, %B %d %Y')} is{wList[-1].weight}lbs.")
    else:
        fr.prLine()
        print("You have not logged your weight today!".center(size.columns))
        print(f"Your weight as of {datetime.datetime.strptime(wList[-1].date, '%Y-%m-%d').date().strftime('%A, %B %d %Y')} is{wList[-1].weight}lbs.".center(size.columns))
        fr.prLine()

def summWeek(weight_file_path):
    fr.prMethodHead("Calculating Average Weight Over the Past Week")
    wList = readList(weight_file_path)
    avgWeight = 0

    if os.path.getsize(weight_file_path) == 0:
        return 0

    if len(wList) < 7:
        for weight in wList:
            print(f"{weight}".center(size.columns))
            avgWeight += float(weight.weight)
        
        avgWeight /= len(wList)
    else:
        for weight in wList[len(wList)-7:len(wList)]:
            print(f"{weight}".center(size.columns))
            avgWeight += float(weight.weight)

        avgWeight /= 7

    print("\n" + f"Your average weight over the past week is {avgWeight:.1f}lbs.".center(size.columns))
    fr.prLine()

def summMonth(weight_file_path):
    fr.prMethodHead(f"Calculating Average Weight Over {datetime.date.today().strftime('%B')}")
    wList = readList(weight_file_path)
    avgWeight = 0

    if os.path.getsize(weight_file_path) == 0:
        return 0
    
    wListMonth = []
    for weight in wList:
        todayMonth = datetime.date.today().strftime("%B")
        wEntryMonth = datetime.datetime.strptime(weight.date, '%Y-%m-%d').date().strftime("%B")
        
        if todayMonth == wEntryMonth:
            wListMonth.append(weight)
    
    for wEntry in wListMonth:
        print(f"{wEntry}".center(size.columns))
        avgWeight += float(wEntry.weight)
    
    avgWeight /= len(wListMonth)

    print("\n" + f"Your average weight over {datetime.date.today().strftime('%B')} is {avgWeight:.2f}lbs.".center(size.columns))
    fr.prLine()

def summYear(weight_file_path):
    fr.prMethodHead(f"Calculating Average Weight Over {datetime.date.today().strftime('%Y')}")
    wList = readList(weight_file_path)
    avgYrWeight = 0

    if os.path.getsize(weight_file_path) == 0:
        return 0

    wYears = {}
    for weight in wList:
        key = datetime.datetime.strptime(weight.date, '%Y-%m-%d').date().strftime("%B")
        if key in wYears:
            wYears[key] = [wYears[key][0] + float(weight.weight), wYears[key][1] + 1]
        else:
            wYears[key] = [float(weight.weight), 1]
    
    # Get average weight over the entire year
    print("Your average weight for each month:".center(size.columns) + "\n")
    for month, weight in wYears.items():
        avgYrWeight += weight[0]
        print(f"{month}: {(weight[0] / weight[1]):.1f}lbs".center(size.columns))
    
    avgYrWeight /= len(wList)
    
    fr.prMethodHead(f"Your average weight in {datetime.date.today().strftime('%Y')} is {avgYrWeight:.1f}lbs.")

def summCalendar(weight_file_path):
    fr.prMethodHead(f"Displaying Weight Over {datetime.date.today().strftime('%Y')}")
    wList = readList(weight_file_path)

    if os.path.getsize(weight_file_path) == 0:
        return 0

    wYears = {}
    for weight in wList:
        key = datetime.datetime.strptime(weight.date, '%Y-%m-%d').date().strftime("%B")
        if key in wYears:
            print(f"[{weight.date}]{weight.weight}lbs".center(size.columns))
            wYears[key] = [wYears[key][0] + float(weight.weight), wYears[key][1] + 1]
        else:
            print("\n" + f"{key}".center(size.columns))
            print(f"[{weight.date}]{weight.weight}lbs".center(size.columns))
            wYears[key] = [float(weight.weight), 1]
    fr.prLine()
