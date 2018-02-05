#Maia Reynolds
#2/2/18
#adventure.py - if statements inside if statements to make adventure

print("You are walking on a sidewalk and reach a crosswalk. You could keep walking or cross the street")
cross=input("Do you cross the street? ")
if cross=="yes":
    print("You did not wait for the light to change and you got hit by a car. Game over")
elif cross=="no":
    print("You continue down the street and reach a tall building")
    enter=input("Do you enter the building? ")
    if enter=="yes":
        print("You enter a lobby and decide to go up to the third floor. You see stairs and an elevator")
        elevator=input("Do you use the elevator? ")
        if elevator=="yes":
            print("You get stuck halfway between the second and third floor. Game over")
        if elevator=="no":
            print("You take the stairs to the third floor and see a red and a blue door")
            red=input("Do you enter the red door? ")
            if red=="yes":
                ...
            elif red=="no":
                ..
            else:
                print("You entered something incorrectly. Game Over")
        else:
            print("You entered something incorrectly. Game Over")
    
    
    elif enter=="no":
        ...
    else:
        print("You entered something incorrectly. Game Over")
else:
    print("You entered something incorrectly. Game Over")