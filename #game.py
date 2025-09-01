#game
print('WELCOME TO TREASURE LAND')
direction=input('select a direction left or right').lower()
if direction=='right':
    print('game over')
elif direction == 'left':
    if input('do you want to swim or wait').lower()=='swim':
        print('game over')
    else:
        if input ('chhoose the color red, blue or yellow').lower()=='yellow':
            print('you won')
        else:
            print('game over')
else:
    print('enter a valid direction')
    