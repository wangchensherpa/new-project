#11.given list is [1,2,3,4] but expected outcome is [1,"a",2,4]
list=[1,2,3,4]
new_list=[]
for i in list:
    if i==2:
        i="a"
    if i==3:
        i-=1
    new_list.append(i)
print("new list is",new_list)