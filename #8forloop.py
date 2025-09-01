#8.given list is [1,2,3,4] but expeected output in new list [2,3,4,5]
list=[1,2,3,4]
new_list=[]
for i in list:
    new_list.append(i+1)
print("new list is:",new_list)