#password
user_name='user12'
password='12344'
for i in range(1,4):
    username=input('enter your username')
    pas=input('enter your password')
    if user_name!=username and password!=pas:
        if(i==3):
         print('too many attempts you are blocked')
        else :
          print('invalid username or password:',3-i,"attempts left")
          break
    else:
        print('you are logged in ')
        break
        
    