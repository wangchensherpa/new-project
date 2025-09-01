#1.while loop
while True:
    age=int(input("enter your age"))
    if age<18:
        print("you are a minor")
    elif age>=18 and age<60:
        print("you are an adult")
    else :
        print("you area sinior citizen")
    a=input("do you want to stop").lower()
    if a=='stop':
        break
        