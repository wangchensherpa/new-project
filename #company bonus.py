#company bonus
salary=float(input('enter your salary'))
years=float(input('enter your years of service'))
if years>5:
    bonus=(salary*(1+0.05))
    print(f'your net salary with bonus is {bonus}')
else:
    print(f'your net salary is {salary}')