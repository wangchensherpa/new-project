#10.given list is lst=[1,2,3,4] but print 1 2 and 4 only
lst=[1,2,3,4]
new_lst=[]
for i in lst:
    if i==3:
        continue
    new_lst.append(i)
print("the new list is",new_lst)