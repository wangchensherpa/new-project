#2movie ticket
age=int(input('enter your age'))
if age <12 :
    print('ticket is free')
elif age>=12 and age<=60 :
    membership_card= input('do you have a membership card yes or no?').lower()
    if membership_card=='yes':
        print('the ticket cost is rs.150')
    else:
        print('the ticket cost isrs.200')
elif age>60:
    print('you get a senior citizen discount and the cost of ticket is rs.100')
else:
    print('enter a valid age')