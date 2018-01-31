#Maia Reynolds
#1/31/18
#fortuneTeller.py - pick color, number, then tells fortune

color=input("Pick red or blue: ")
number=int(input("Pick an number from 1-4: "))
if color=="blue" or color=="Blue" and number==1:
    print("You will find your keys")
elif color=="blue" or color=="Blue" and number==2:
    print("You will slip on the ice")
elif color=="blue" or color=="Blue" and number==3:
    print("Your phone screen will crack")
elif color=="blue" or color=="Blue" and number==4:
    print("You will eat a bagel")
elif color=="red" or color=="Red" and number==1:
    print("You will fail your next math test")
elif color=="red" or color=="Red" and number==2:
    print("You will meet a cute dog")
elif color=="red" or color=="Red" and number==3:
    print("You will need to visit the tech department soon")
elif color=="red" or color=="Red" and number==4:
    print("You will will the lottery")
else:
    print("You entered something incorrectly")