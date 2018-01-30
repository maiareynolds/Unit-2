#Maia Reynolds
#1/30/18
#movie.py - tells user what movie they can watch

age=int(input("Enter your age: "))
if age<13:
    print("You can watch PG movies")
elif age<17:
    print("You can watch PG-13 movies")
else:
    print("You can watch R movies")