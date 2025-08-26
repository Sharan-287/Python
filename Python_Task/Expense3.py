import os
from datetime import datetime

filename="Expense Log.txt"

def addexpense():
    date=datetime.now().strftime("%y-%m-%d")
    description=input("Enter Description:")
    category=input("Enter category(like Travel, Food, Shopping etc..,):")

    try:
        amount=float(input("Enter a Amount:"))
    except ValueError:
        print("The must be in Number")
        return
    file=open("Expense Log.txt","a")
    file.write(f"{date},{description},{category},{amount}\n")
    print("The Expense was added Successfully")

def veiwexpense():
    if not os.path.exists("Expense Log.txt"):
        print("The Expence Log is Missing")
        return
    file=open("Expense Log.txt", "r")
    print("\n--- All Expenses ---")
    for line in file:
        date, desc, cat, amt = line.strip().split(",")
        print(f"{date} | {desc} | {cat} | Rs.{amt}")

def totalex():
    if not os.path.exists("Expense Log.txt"):
        print("The Expence Log is Missing")
        return
    total=0
    file=open("Expense Log.txt","r")
    print("\n---Total Expense---")
    for line in file:
        total+=float(line.strip().split(",")[3])
        print(f"Total amount is:{total}")

def menu():
    while True:
        print("\n---EXPENSE TRACKER---")
        print("1.Add Expense:")
        print("2.View All Expenses")
        print("3.View Total Spending")
        print("4.Exit")

        choice=int(input("Enter the Option:"))

        if choice == 1:
            addexpense()
        elif choice == 2:
            veiwexpense()
        elif choice == 3:
            totalex()
        elif choice == 4:
            print("THANK YOU")
            break
        else:
            print("Invalid Option!")
menu()