#file handling
# try:
#     filename='ab.txt'
#     f=open(filename,'r')
# except:
#     print(f'{filename} is not available')
    
    
    
# filename='abc.txt'
# f=open(filename,'w')
# f.write('123')
# f.write('python')
# f.close()

# fruits=['apple','banana','orange']   
# filename='abc.txt'
# f=open(filename,'w')
# print(f.name)
# print(f.mode)
# print(f.closed) # gives answer in boolen true or false
# print(f.readable())
# print(f.writable())
# for i in fruits:
#   f.writelines(i+'\n')
# f.close()

# fruits=['apple','banana','orange']   
# filename='abc.txt'
# try:
#     f=open(filename,'x')
# except:
#     print(f'{filename}name is already available')
#     f=''
# else:
#     f.writelines(fruits)
# finally:
#     if f:
#         f.close()
 
# filename='abc.txt'
# f=open(filename,'r')
# print(f.read(4))
# print(f.read())
# f.close()


# filename='abc.txt'
# f=open(filename,'r')
# count=0
# for i in f:
#     count+=1
#     if count==2 or count==4:
#         print(i,end='')
# f.close()


# filename='abc.txt'
# f=open(filename,'r')
# print(f.readline(1))
# print(f.readline(1))
# print(f.readline())
# f.close()


# ff=[]
# filename='abc.txt'
# f=open(filename,'r')
# for i in f:
#     c=i.strip()
#     ff.append(c)    
# print(ff)
# f.close()

# filename='abc.txt'
# f=open(filename,'r')
# f.read(4)
# print(f.read())
# f.close()


# filename='abc.txt'
# f=open(filename,'r')
# print(f.tell())
# f.seek(4)
# print(f.read())
# f.close()

# filename='abc.txt'
# f=open(filename,'r')
# print(f.tell())
# f.seek(4)
# print(f.read(7))
# f.close()


# filename='abc.txt'
# f=open(filename,'r+')
# print(f.read())
# f.write('program')
# f.close()

# filename='afffc.txt'
# fruits=['apple','orange','grapes']
# f=open('ab.txt','wb')
# import pickle
# pickle.dump(f)
# print(c)
# f.close()


f=open('softwarica.txt')
f2=open('softwarica1.txt','w')
for i in f:
    c=i.strip().split()
    f2.write(c[1])

