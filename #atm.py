#atm
pin=1234
actual_balance=20000
user_input=int(input('please enter your pin'))
if user_input==pin:
    print('1.check balance')
    print('2.withdraw money')
    print('3.deposit money')
    print('4.exit')
    choice=int(input('enter a choice:'))
    if choice==1:
     print(f'your balance is {actual_balance}')
    elif choice==2:
        withdraw_amount=int(input('enter a amount'))
        if withdraw_amount <=0 or withdraw_amount >actual_balance:
            print('enter a valid amount')
        else:
            actual_balance= actual_balance - withdraw_amount
            print(f'remaing amount is{actual_balance} ')
    elif choice==3:
        deposit_amount=int(input('enter a amount') )
        if deposit_amount <0:
            print('enetr a valid amount')
        else:
            actual_balance= actual_balance + deposit_amount
            print(f'the final amount is{actual_balance}')
    elif choice==4:
        print('thank you for visiting')
    else:
        print('please enter a valid option')
else:
    print('enter a valid pin')
    
    
    