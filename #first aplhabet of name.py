#first aplhabet  of name
for row in range(6):
    for column in range(5):
        if (column==0):
            print('*',end=' ')
        elif(column ==1 or column ==2 or column==3)\
            and(row==0 or row==3 ):
                print('*',end=' ')
        elif(column==4) and(row==1 or row==2):
            print('*',end=' ')
        else:
            print(end='  ')
    print()