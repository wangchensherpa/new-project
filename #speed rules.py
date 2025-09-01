#speed rules
speed=int(input('enter your speed'))
if speed<=60:
    print('no fine')
elif speed>60 and speed<80:
    licence=input('do you have a licence yes or no?').lower()
    if licence=='yes':
        print('your fine is rs. 500')
    else:
        print('your fine is rs.1000')
elif speed>80:
    print('your fine is rs.3000')
     