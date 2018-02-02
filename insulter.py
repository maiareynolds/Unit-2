#Maia Reynolds
#2/2/18
#insulter.py - gives insult

from random import randint
name=input("Enter your name: ")
number=randint(1,5)
if number==1:
    print(name,"is a stupid name")
elif number==2:
    print("You have horrible taste")
elif number==3:
    print("You smell disgusting")
elif number==4:
    print("You are such an idiot")
else:
    print("Your shirt is ugly")