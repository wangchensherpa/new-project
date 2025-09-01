#youngest one 
a=int(input('enter the age of 1st person'))
b=int(input('enter the age of 2nd person'))
c=int(input('enter the age of 3rd person'))
d=int(input('enter the age of 4th person'))
if a<b<c<d:
    print('the 1st person is the youngest')
elif b<a<c<d:
    print('the 2nd person is the yongest')
elif c<a<b<d:
    print('the 3rd person is the youngest')
else:
    print('the 4th person is the youngest')