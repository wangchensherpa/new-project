import random
a = input("Guess a number between 1 and 10 ")
b = random.randint(1,10)
if a == b:
    print("You are correct")
else:
    print("You fail")