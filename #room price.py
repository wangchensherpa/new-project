#room price
guest_type=input('are you a member yes or no?').lower()
if guest_type=='yes':
    season=input('is season peak yes or no').lower()
    if season=='yes':
        print('the price of room is rs.4000')
    else:
        print('the price of room is rs.3000')
elif guest_type=='no':
    season=input('is season peak yes or no?')
    if season=='yes':
        print('the price is rs.5000')
    else:
        print('the price is 3500')
        