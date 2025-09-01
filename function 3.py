# #function 3 very important for exam
# l=20 #global variable
# def area_of_reactangle(length,bredth):
#     def inner():
#         global l #to modify a global variable
#         l=l+5
#         print(l)
#     print(l)#20
#     inner()#25
#     print(l)#25
# area_of_reactangle(10,20)

# l=20
# def area_of_reactangle(length,bredth):
#     b=40 #enclosed variable
#     def inner():
#         global l
#         l=l+5
#         nonlocal b #to modify a enclosed variable
#         b=b+70
#         print(l)
#     print(l)#20
#     print(b)#40
#     inner()#25
#     print(l)#25
#     print(b)#110
# area_of_reactangle(10,20)

#suppose there are two programs in softwarca college : computer science and cyber security , 
# therea rae two modules in computer science ;python and software desighn and there is one module
# in cyber security ; computer archetucture. ram teaches python so he should not be able to access
# other two modules likewise other two teacher syam and hari respectively.

# def computer_science():
#     def python_module():
#         teacher=input("enter a teacher's name for python module ").lower()
#         if teacher=='ram':
#             print('access granted in python module')
#         else:
#             print('access deniedin python module')
#     python_module()   
#     def software_desighnmodule():
#         teacher=input("enter a teacher's name for software desighn module").lower()
#         if teacher=='syam':
#             print('access granted in software desighn module')
#         else:
#             print('access denied in software desighn module')
#     software_desighnmodule()
# computer_science()    
# def cybersecuity():
#     def computer_archetecture():  
#         teacher=input("enter a teacher's name for cyber security module ").lower()
#         if teacher=='hari':
#          print('access granted in cyber security module')
#         else:
#             print('access denied in cyber security module')
#     computer_archetecture() 
# cybersecuity()


def computer_science():
    def python_module():
        teacher=input("enter your name ").lower()
        module=input("enter your module name")
        if teacher=='ram' and module=='python':
            print(f'access granted in python module for{teacher} sir.')
        else:
            print('access deniedin python module')
    python_module()   
    def software_desighnmodule():
        teacher=input("enter your name").lower()
        module=input("enter your module name").lower()
        if teacher=='syam' and module=='software desighn':
            print(f'access granted in software desighn module for {teacher} sir.')
        else:
            print('access denied in software desighn module')
    software_desighnmodule()
  
def cybersecuity():
    def computer_archetecture():  
        teacher=input("enter ypur name ").lower()
        module=input("enter your module name").lower()
        if teacher=='hari' and module=='cyber security':
         print(f'access granted in cyber security module for {teacher} sir.')
        else:
            print('access denied in cyber security module')
    computer_archetecture() 

department=input("which department are you from?")
if department=='computer science':
    computer_science()
elif department=='cyber security':
    cybersecuity()
else:
    print("there is no such department")