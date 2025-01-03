import os

size = os.get_terminal_size()

def prLine():
    print("\n" + "=" * size.columns + "\n")

def prProgHead():
    size = os.get_terminal_size()

    prLine()
    print("Weight Tracker v1.4.0".center(size.columns))
    print("A Python program to track your calories, protein intake, and weight.".center(size.columns))
    print("-----------------------------------------------".center(size.columns))
    print("Created by Aaron Ramos (ramosaaron2@gmail.com)".center(size.columns))
    print("Based on 'Expense Tracking App' Project by pixegami".center(size.columns))
    prLine()

def prMethodHead(text):
    prLine()
    print(f"--- {text} ---".center(size.columns))
    prLine()

def prErrorMes(text):
    print("\n" + ("x" * int(size.columns/2)).center(size.columns) + "\n")
    print(f"ERROR: {text}".center(size.columns))
    print("\n" + ("x" * int(size.columns/2)).center(size.columns) + "\n")
