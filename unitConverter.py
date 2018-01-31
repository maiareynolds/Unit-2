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
    print(kg,"kilograms is",round(kg*2.20462,5),"pounds")
elif number==3:
    l=int(input("Enter volume in liters: "))
    print(l,"liters is",round(l*0.264172,5),"gallons")
elif number==4:
    c=int(input("Enter degrees in Celcius: "))
    print(c,"degrees Celcius is",round((c*1.8)+32,5),"degrees Fahrenheit")
else:
    print("Wrong Number, Try Again")