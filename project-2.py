from tkinter import *
from tkinter import messagebox
top=Tk()
top.title('Log in')
top.geometry('600x600')
Label(text='login').pack(side=TOP)
Label(text='username').place(x=20,y=40)
username_entry=Entry(top)
username_entry.place(x=90,y=40)
Label(text='password').place(x=20,y=80)
password_entry=Entry(top,show="*")
password_entry.place(x=90,y=80)
def login():
    username=username_entry.get()
    password=password_entry.get()
    if username =="admin" and password=="123":
        messagebox.showinfo("login","Login sucessful")
    else:
         messagebox.showinfo("login","Invalid username or password")

def signup():
    signup_window=Toplevel(top)
    signup_window.title("sign Up")
    signup_window.geometry("300x300")
    
    Label(signup_window, text= "E-mail").place(x=20,y=20)
    signup_email=Entry(signup_window)
    signup_email.place(x=130,y=20)
    Label(signup_window, text= "Password").place(x=20,y=60)
    signup_password=Entry(signup_window)
    signup_password.place(x=130,y=60)
    Label(signup_window, text="Create Username").place(x=20,y=100)
    signup_username=Entry(signup_window)
    signup_username.place(x=130,y=60)

    Label(signup_window, text="Create Password").place(x=20,y=140)
    signup_newpassword=Entry(signup_window, show="*")
    signup_newpassword.place(x=130,y=60)
    Button(signup_window, text="Submit").place(x=20,y=180)

    
           
Button(top,text='login',command=login).place(x=90,y=120)
Button(top,text="sign up", command=signup).place(x=160,y=120)
top.mainloop()