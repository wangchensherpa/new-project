# num=int(input("Enter a number:"))
# check=num
# length=len(str(num))
# Sum=0
# for i in range(length):
#
#     temp=check %10
#     Sum=temp**length+Sum
#     check=check//10
# if Sum==num:
#     print("{} is armstrong".format(num))
# else:
#     print("{} is not armstrong".format(num))

# bad=[';',":","!","*"]
# string="py;th*o:n!py*t*h:o!n"
# removed=[]
# count=0
# while count<len(string):
#     if string[count] not in bad:
#         removed.append(string[count])
#     count+=1
# print("".join(removed))

# arthematic quiz


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
    