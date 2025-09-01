# from tkinter import * #important
# root=Tk()
# root.title('login')
# root.geometry('300x300') #if used geometry the height and width can be changed without limit so maxsize and minsize
# root.maxsize(width=300,height=300)
# root.minsize(width=200,height=200)
# root.resizable(0,0) #removes the size icon from the window as false and false of height and width if used 1,0 width can be changes but not height and vise versa.
# Label(text='facebook').pack(expand=True) #side=bottom for bottom , side =left for left and so on
# mainloop()

# from tkinter import *
# root=Tk()
# root.title('side')
# root.geometry('500x500')
# root.maxsize(width=300,height=300)
# root.minsize(width=200,height=200)
# root.resizable(0,0)
# Label(text='top').pack(side=TOP)
# Label(text='bottom').pack(side=BOTTOM)
# Label(text='right').pack(side=RIGHT)
# Label(text='left').pack(side=LEFT)
# Label(text='center').pack(expand=True)
# mainloop()

# from tkinter import * # grid for using row and column
# root =Tk()
# name=Label(root,text="Name").grid(row=0,column=0)
# el=Entry(root).grid(row=0,column=1)
# password=Label(root,text="password").grid(row=1,column=0)
# e2=Entry(root).grid(row=1,column=1)
# submit=Button(root,text="submit").grid(row=4,column=1)
# root.mainloop()

# from tkinter import * 
# top=Tk()
# top.geometry("400x500")
# name=Label(top,text="Name").place(x=30,y=50)
# address=Label(top,text="Address").place(x=30,y=90)
# contact=Label(top,text="Contact").place(x=30,y=130)
# e1=Entry(top).place(x=80,y=50)
# e2=Entry(top).place(x=80,y=90)
# e3=Entry(top).place(x=95,y=130)
# top.mainloop()

# from tkinter import *
# top=Tk()
# top.title('login')
# top.geometry("500x600")
# Label(text="Registration").pack(side=TOP)
# fullname=Label(top,text="Full name")
# fullname.place(x=30,y=50)
# lastname=Label(top,text="Last name")
# lastname.place(x=30,y=90)
# email=Label(top,text="E-mail")
# email.place(x=30,y=135)
# phoneno=Label(top,text="phone no.")
# phoneno.place(x=30,y=180)
# e1=Entry(top)
# e1.place(x=100,y=50)
# e1=Entry(top)
# e1.place(x=100,y=90)
# e1=Entry(top)
# e1.place(x=80,y=135)
# e1=Entry(top)
# e1.place(x=90,y=180)
# top.mainloop()

 #disadvantage of entry( ) is that it is only used for small texts not for fulll paragraphs and only in line . so we use Text ()instead.
# from tkinter import *
# root = Tk()
# root.geometry('500x500')
# ent =Text() # this is entry box
# ent.pack()
# lbl=Label(text='ram')
# lbl.pack()
# def sum():
#     lbl.config(text=ent.get('1.0' ,'1.1')+ent.get('2.0','2.1')) # helps rewrite the output in same line
#     ent.delete('1.0',END) # clears the input box
# btn=Button(text="submit",command=sum) # here command is used to call the function
# btn.pack()
# mainloop()


# from tkinter import *
# root = Tk()
# root.geometry('500x500')
# def gender():
#     lbl.config(text=r.get())
# r=IntVar()
# r1=Radiobutton(text='male',value=0,variable=r,command=gender) #variable=r is used to connect r with r1 annd so on
# r1.pack()
# r2=Radiobutton(text='female',value=1,variable=r,command=gender)
# r2.pack()
# r3=Radiobutton(text='others',value=2,variable=r,command=gender)
# r3.pack()
# lbl=Label(text='')
# lbl.pack()

# mainloop()


# from tkinter import *
# root = Tk()
# root.geometry('500x500')
# def gender():
#     lbl.config(text=r.get())
# r=StringVar()     #example of stringvar()
# r1=Radiobutton(text='male',value='you have seleted male',variable=r,command=gender) #variable=r is used to connect r with r1 annd so on
# r1.pack()
# r2=Radiobutton(text='female',value='you have seleted female',variable=r,command=gender)
# r2.pack()
# r3=Radiobutton(text='others',value='you have seleted others',variable=r,command=gender)
# r3.pack()
# lbl=Label(text='')
# lbl.pack()
# mainloop()

# from tkinter import * #alternate method of above program using if else.
# root = Tk()
# root.geometry('500x500')
# def gender():
#     if r.get()==0:
#         lbl.config(text='you have seleted male')
#     elif r.get()==1:
#         lbl.config(text='you have seleted female')
#     else:
#         lbl.config(text='you have seleted others')
# r=IntVar()
# r1=Radiobutton(text='male',value=0,variable=r,command=gender) #variable=r is used to connect r with r1 annd so on
# r1.pack()
# r2=Radiobutton(text='female',value=1,variable=r,command=gender)
# r2.pack()
# r3=Radiobutton(text='others',value=2,variable=r,command=gender)
# r3.pack()
# lbl=Label(text='')
# lbl.pack()

# mainloop()



# from tkinter import * 
# root = Tk()
# root.geometry('500x500')
# def gender():
#     lbl.config(text=r.get())
# r=IntVar()
# r1=Checkbutton(text='football',variable=r,command=gender) # checkbutton passes 2 values on=1,off=0 automatically so it is diff fromradiobutton and in check you can select multiple options as well
# r1.pack()

# lbl=Label(text='')
# lbl.pack()
# mainloop()


# from tkinter import * 
# root = Tk()
# root.geometry('500x500')
# def gender():
#     if r.get()==1 and y.get()==1:
#         lbl.config(text='you have selected both')
#     elif y.get()==1:
#         lbl.config(text='you have selected basketball')
#     elif r.get()==1 :
#         lbl.config(text='you have selcted football')
        
# r=IntVar()
# r1=Checkbutton(text='football',variable=r,command=gender) 
# r1.pack()
# y=IntVar() #for different check button there must be different class.
# r2=Checkbutton(text='basketball',variable=y,command =gender)
# r2.pack()
# lbl=Label(text='')
# lbl.pack()
# mainloop()

# from tkinter import *
# root=Tk()
# root.geometry('500x500')
# ent=Entry(show='*')
# ent.place(x=20,y=40)
# def password():
#     if r.get()==1:
#         ent.config(show='')
#     else:
#         ent.config(show='*')
# r=IntVar()
# btn1=Checkbutton(text='show password',variable=r,command=password)
# btn1.place(x=50,y=80)
# mainloop()


# r2.pack()
# r2.pack()


# from tkinter import*
# from math import*
# from tkinter import messagebox
# root=Tk()
# root.geometry('300x300')
# root.resizable(0,0)
# length=Entry()
# length.pack()
# bredth=Entry()
# bredth.pack()
# lbl=Label(text='')
# lbl.pack()
# radius=Entry()
# radius.pack()
# def areaofrectangle():
#     area=int(length.get())*int(bredth.get())
#     lbl.config(text=area)
#     length.delete(0,END)
#     bredth.delete(0,END)
# def areaofcirclr():
#     r=float(radius.get())
#     area=pi*r*r
#     lbl.config(text=area)
# btn=Button(text='calculate',command=areaofrectangle)
# btn.pack()
# btn1=Button(text='area of circlee',command=areaofcirclr)
# btn1.pack()
# mainloop()


# from tkinter import*
# top=Tk()
# top.title('login')
# top.geometry("500x600")
# Label(text="Registration").pack(side=TOP)
# username=Label(top,text="user name")
# username.place(x=30,y=50)
# password=Label(top,text="password")
# password.place(x=30,y=90)
# e1=Entry(top)
# e1.place(x=100,y=50)
# e1=Entry(top)
# e1.place(x=100,y=90)
# e1=Entry(top)
# login_btn=Button(text='login')
# login_btn.place(x=100,y=130)
# registerbutton=Button(text='create account')
# registerbutton.place(x=100,y=150)

# def login():
#     register_email.pack_forget()
#     register_btn.pack_forget()
#     back_to_login_btn.pack_forget()
#     login_username.pack()
#     login_password.pack()
#     login_btn.pack()
#     register_btn.pack()
        
# def register():
#     login_username.pack_forget()
#     login_password.pack_forget()
#     login_btn.pack_forget()
#     register_btn.pack_forget()
#     register_email.pack()
#     register_password.pack()
#     register_btn.pack()
#     back_to_login_btn.pack()

# login_username=Entry()
# login_password=Entry()
# login_btn=Button(text='LOGIN')
# register_email=Entry()
# register_password=Entry()
# register_btn=Button(text='craete account',command=register)
# back_to_login_btn=Button(text='back to login',command=login)

# login()   
top.mainloop()