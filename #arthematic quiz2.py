#arthematic quiz
import random
a= random.randint(1,30)
b= random.randint(1,30)
count=1
totalscore=0
while True:
    c=int(input(f"enter the multipilication of {a} and {b}"))
    final_result=a*b
    if c==final_result:
        print("correct! ")
        totalscore+=1
        again=input("do you want to play again yes or no").lower()
        if again=='yes':
            a= random.randint(1,30)
            b= random.randint(1,30)
        else:
            break   
    else:
        if count==3:
            break
        print("incorrect ! try again")
        count+=1
print(totalscore)
    