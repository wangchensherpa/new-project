#4.while loop
password='password'
while True:
    a=input("enter the password")
    if a==password:
        print("access garnted")
    else:
        print("wrong password ,try again")
    b=input("do you want to open sesame").lower()
    if b=='open sesame':
        break