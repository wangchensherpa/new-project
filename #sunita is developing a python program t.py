#sunita is developing a python program to help people konow if they are eligible to vote for her country .according to the law a person must be at least 18 and musr be a citizen of the country (ansering yes to citizenship)
age=int(input('enter your valid age'))
if age>=18:
    citizen_ship=input('which country arre you from').lower()
    if citizen_ship=='nepal' :
        print('yes you are eligible to vote')
    else:
        print('you are not eligible to vote')
else:
    print('age must be atleast 18')