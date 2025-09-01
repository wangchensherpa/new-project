#given list is[1,2,3,"d",4,5"a"] seperate the elements based on their data types.
list=[1,2,3,"d",4,5,"a"]
integer_list=[]
string_list=[]
for i in list: 
    if isinstance(i,int):
        integer_list.append(i)
    else: 
        isinstance(i,str)
        string_list.append(i)
print(integer_list)
print(string_list)