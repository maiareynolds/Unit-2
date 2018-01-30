#Maia Reynolds
#1/30/18
#gradeCalculator.py - percentage to letter grade

grade=int(input("Enter your grade as a percent: "))
if grade>=90:
    print("You earned a A")
elif grade>=80:
    print("You earned a B")
elif grade>=70:
    print("You earned a C")
elif grade>=60:
    print("You earned a D")
else:
    print("You earned a NC")