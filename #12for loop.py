#12.given list is [1,2,3,4,5] seperate the elements into odd and even categories.
list=[1,2,3,4,5]
odd=[]
even=[]
for i in list:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print("even numbers are:",even)
print("odd numbers are:",odd)