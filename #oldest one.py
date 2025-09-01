#oldest one 
a=int(input('enter the age of 1st person'))
b=int(input('enter the age of 2nd person'))
c=int(input('enter the age of 3rd person'))
d=int(input('enter the age of 4th person'))
if a>b and a>c  and a>d:
    print('the 1st person is the oldest')
elif b>a and b>c and b>d:
    print('the 2nd person is the oldest')
elif c>a and c>b and c>d:
    print('the 3rd person is the oldest')
else:
    print('the 4th person is the oldest')