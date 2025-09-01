# #function1

# def area_rectange():
#     l=int(input('enter a length'))
#     b=int(input('enter a bredth'))
#     area=l*b
#     print(area)
# area_rectange()



# def area_rectange(l,b):
#     area=l*b
#     print(area)
# l=int(input('enter a length'))
# b=int(input('enter a bredth'))
# area_rectange(l,b)


# def area_rectange(l,b):
#     area=l*b
#     print(area)
# area_rectange(20,10)
# area_rectange(50,60)

# def area_rectange(l,b=10): #here defult value of b is set so there is no need to pass bredths argument in calling.
#     area=l*b
#     print(area)
# area_rectange(20)


# def area_rectange(l,b=10):
#     area=l*b
#     return area
# print(area_rectange(20))

# def area(*b):
#     area=b
#     sum=0
#     for i in area:
#         sum=sum+i
#     print(sum)
# area(10,20,30)

# def area(*b):
#     area=b
#     for i in area:
#         for j in range(1,11):
#             print(i,'x',j,'=',i*j)
#         print()    
# if __name__ == "__main__":   # helps hide the statement from other files which are importing this file.
#  area(10,20,30)



# def area(*b):
#     area=b
#     return(area)
# c=area(10,20,30)
# print(c)

# def multiplication(c):
#     for i in c:
#         for j in range(1,11):
#             print(i,'x',j,'=' ,i*j)
#         print()
# multiplication(c)

# def login(**a):
#     for i in a :
#         print(i)
# login(a=10,b=10,c=20,d=30)

# items=['4+','4+','3+','5+','6+','6+']
# ratings={}

# for i in items:
#     if i in ratings:
#             ratings[i]+=1
#     else:
#             ratings[i]=1
# print(ratings)   

items=['4+','4+','3+','5+','6+','6+']
ratings={}

for i in items:
    if i in ratings:
            ratings[i]+=1
    else:
            ratings[i]=1
count=0
for i in ratings.values():
    for j in range(1,11):
        if i==1:
            print(i,'x',j,'=',i*j)
            if count==1:
                break
        
       
        else:
            print(i,'x',j,'=',i*j)
    count+=1