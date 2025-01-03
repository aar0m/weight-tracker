"""
///                        -------------------------
///                              Weight Tracker
///                        -------------------------
///                           By Aaron Ramos 2025
///
/// Main Python file to run for logging and viewing calories, protein, and weight.
/// Based on 'Expense Tracking App' Project by pixegami
///
/// @file weight-tracker.py
/// @author Aaron Ramos (ramosaaron2@gmail.com)
///
"""

from datetime import datetime
from pathlib import Path
import datetime
import format as fr
import calfunc as cal
import weightfunc as weight

def main():
    fr.prProgHead()

    Path(f"tracker-sheets/calorie/calories{datetime.date.today().strftime('%Y')}").mkdir(parents=True, exist_ok=True)
    cal_dir_path = f"tracker-sheets/calorie/calories{datetime.date.today().strftime('%Y')}"
    cal_file_path = f"tracker-sheets/calorie/calories{datetime.date.today().strftime('%Y')}/calories{datetime.date.today().strftime('_%m-%Y')}.csv"
    weight_file_path = f"tracker-sheets/weight/weight{datetime.date.today().strftime('%Y')}.csv"
    
    options = ["Log Calories", "View Calories", "Log Weight", "View Weight", f"View {datetime.date.today().strftime('%Y')} Food Log", "Exit"]

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
                food = cal.getCal()
                cal.saveCal(food, cal_file_path)
            case 1:
                try:
                    cal.calInterface(cal_file_path)
                except FileNotFoundError:
                    fr.prErrorMes(f"You have not logged any calories for {datetime.date.today().strftime('%B %Y')}!")
                    exit
            case 2:
                recWeight = weight.getWeight()
                weight.save(recWeight, weight_file_path)
            case 3:
                try:
                    weight.weightInterface(weight_file_path)
                except FileNotFoundError:
                    fr.prErrorMes(f"You have not logged any weights for {datetime.date.today().strftime('%Y')}!")
                    exit
            case 4:
                try:
                    cal.summFood(cal_dir_path)
                except FileNotFoundError:
                    fr.prErrorMes(f"You have not logged any calories for {datetime.date.today().strftime('%B %Y')}!")
                    exit
            case 5:
                print("Exiting Now".center(32, "-"), "\n")
                break
            case _:
                fr.prErrorMes(f"Invalid input. Please enter a value from {possVal}.")

if __name__  == "__main__":
    main()