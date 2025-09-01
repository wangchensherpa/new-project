#14.eligible for voting or not.
age=int(input('enter your age'))
if age>=18:
    citizenship=input('are you a citizen of this country yes or no ').lower()
    if citizenship=='yes':
        print('you are eligible to vote')
    else:
        print('you are not eligible to vote')
else:
    print('you must be about 18 years to vote')