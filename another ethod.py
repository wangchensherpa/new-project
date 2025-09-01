user_input=int(input('enter a valid number'))
days = {1: 'sunday',2: 'monday',3: 'tuesday'}
if user_input in days:
    Output=days[user_input]
    print('Output')
else :
    print('invalid number')