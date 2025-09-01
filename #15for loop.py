#15.pytgon program to accept a string and calculate the number of its digits and letters
a=input("enter a string")
sum=[]
count=0
for i in range(len(a)):
    try:
         k= int (a[i])
         sum.append(k)
     
    except:
        count=count+1
        if count==1:
         print('something went wrong')
        
    
print(sum)