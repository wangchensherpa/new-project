#18.wages according to age , gender and number of days 
age=int(input('enter your age'))
if age>=18 and age<30:
    gender=input(' enter your gender as male and female m and f').lower()
    if gender=='m':
        print('your  wage per day is 700')
    elif gender=='f':
        print('yor wage per day is 750')
elif age>=30 and age<=40:
     gender=input(' enter your gender as male and female m and f').lower()
     if gender=='m':
            print('your  wage per day is 800')
     elif gender=='f':
            print('yor wage per day is 850')
else:
    print('enter a valid age')

        