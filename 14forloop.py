#14.list=[1,2,3,4,"a","b"]append each elements data types to seperate lists.
list=[1,2,3,4,"a","b"]
int_list=[]
str_list=[]
for i in list:
    if isinstance(i,int):
        int_list.append(i)
    elif isinstance(i,str):
        str_list.append(i)
print("integer list are:",int_list)
print("string list are: ",str_list)