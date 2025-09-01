#2total bill
electricity_usage=int(input('enter your electricity usage in units'))
if electricity_usage <100 :
    amount=electricity_usage*5
    print(f'total amount to pay is {amount}')
elif electricity_usage>=100 and electricity_usage <=300:
    amount=100*5 + (electricity_usage-100)*8
    print(f'tatal amount to pay is  {amount} ')
elif electricity_usage> 300:
    amount=100*5 +200*8 +(electricity_usage -300)*10
    print(f'total amount to pay is {amount}')
    