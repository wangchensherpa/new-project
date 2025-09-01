#9.fiven list is lst=[1,2,3,4] but print 1 and 4 only.
list=[1,2,3,4]
new_list=[]
for i in list:
    if i==2 or i==3:
        continue
    new_list.append(i)
print("new list is:",new_list)