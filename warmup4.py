#Maia Reynolds
#2/2/18
#warmup4.py - ask user for number, print if divisible by 7 or has a 7, or print number

number=int(input("Enter a number: "))
if number%7==0 or "7" in str(number):
    print("Buzz")
else:
    print(number)