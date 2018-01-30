#Maia Reynolds
#1/30/18
#oddEven.py - tells if number is odd or even

number=int(input("Enter a number: "))
if number==0:
    print(number,"is zero")
elif number%2==0:
    print(number,"is even")
else:
    print(number,"is odd")