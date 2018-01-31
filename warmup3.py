#Maia Reynolds
#1/31/18
#warmup3.py - print out if divisible by 2,3,neither,both

number=int(input("Enter a number: "))
if number%2==0 and number%3==0:
    print(number,"is divisible by both 2 and 3")
elif number%3==0:
    print(number,"is divisible by 3")
elif number%2==0:
    print(number,"is divisible by 2")
else:
    print(number,"is not divisible by 2 or 3")