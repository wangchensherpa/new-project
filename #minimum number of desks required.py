#minimum number of desks required
a=int(input('enter the number of students in class a '))
b=int(input('enter the number of students in class b '))
c=int(input('enter the number of students in class c '))
x=(a+1)//2
y=(b+1)//2
z=(c+10)//2
total_desks=x+y+z
print(f'the minimum desks to be purchased is{total_desks}')