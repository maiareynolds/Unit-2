#Maia Reynolds
#2/12/18
#quiz2.py - 2nd quiz

#Part 1: Words
word1=input("Enter your first word: ")
word2=input("Enter your second word: ")
first=len(word1)
second=len(word2)

if first>second:
    print(word1,"is longer than",word2)
elif word1==word2:
    print(word1,"is the same word as",word2)
elif second>first:
    print(word2,"is longer than",word1)
else:
    print(word1,"is the same length as",word2)

if "p" in word1 and "p" in word2:
    print("Both",word1,"and",word2,"have the letter p in them")
elif "p" in word1:
    print(word1,"has the letter p in it")
elif "p" in word2:
    print(word2,"has the letter p in it")
else:
    print(word1,"and",word2,"do not have the letter p in them")

#Part 2: Numbers
print("Enter two numbers that add up to 12")
number1=int(input("First Number: "))
number2=int(input("Second Number: "))

if number1+number2==12:
    print("Correct")
else:
    print("Incorrect")