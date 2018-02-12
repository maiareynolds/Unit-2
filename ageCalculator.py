#Maia Reynolds
#2/12/18
#ageCalculator.py - tells age from date

from datetime import date
currentday=date.today().day
currentmonth=date.today().month
currentyear=date.today().year
year=int(input("Enter the year you were born: "))
month=int(input("Enter the month you were born: "))
day=int(input("Enter the day you were born: "))
if month>currentmonth:
    print("You are",currentyear-year-1,"years old")
elif month==currentmonth:
    if day>currentday:
        print("You are",currentyear-year-1,"years old")
    elif day<currentday:
        print("You are",currentyear-year,"years old")
    else:
        print("You are",currentyear-year,"years old")
        print("Happy Birthday!")
else:
    print("You are",currentyear-year,"years old")