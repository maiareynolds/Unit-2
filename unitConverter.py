#Maia Reynolds
#1/30/18
#unitConverter.py - user pick unit conversion, convert units

print("1) Kilometers to Miles")
print("2) Kilograms to Pounds")
print("3) Liters to Gallons")
print("4) Celcius to Fahrenheit")
number=int(input("Choose a number: "))
if number==1:
    km=int(input("Enter distance in kilometers: "))
    print(km,"kilometers is",round(0.621371*km,5),"miles")
elif number==2:
    kg=int(input("Enter weight in kilograms: "))
    print(kg,"kilograms is",round(kg*
elif number==3:
    l=int(input("Enter volume in liters: "))
elif number==4:
    c=int(input("Enter degrees in celcius: "))