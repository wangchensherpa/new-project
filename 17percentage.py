#17.class attended.
days=int(input('enter the number of total days'))
absent=int(input('enter the number of total absent days'))
percentage=absent/days*100
percent=100-percentage
if percent<75:
    print('you are not eligible to sit in exam')
else:
    print('you are eligible to sit in exam')