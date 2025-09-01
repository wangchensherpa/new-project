#16.mathematical operators 
a=int(input('enter the firts number'))
b=int(input('enter the second number'))
operator=input('enter operator(+,-,*,/)')
if operator=='+':
    result=a+b
    print(f'your answer is{result}')
elif operator =='-':
    result=a-b
    print(f'your answer is{result}')
elif operator=='*':
    result=a*b
    print(f'the answer is{result}')
elif operator == '/':
    result=a/b 
    print(f'the answer is{result}')
else:
    print('enter the correct operator')