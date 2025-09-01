from tkinter import *
from tkinter import ttk as ttk
import sqlite3
from tkinter import messagebox

def login():
    top=Tk()
    top.geometry('600x600')
    top.title('Login  page')
    parent=ttk.Frame(top,width=600,height=600)

    def page_switcher(Frame):
        
        Frame.tkraise()
    page_switcher(show_login(parent,page_switcher))
        
   
    mainloop()   
    
        
def  show_login(frame,page_switcher):
    login_frame = ttk.Frame(frame,width=600,height=600)
       
    
    Label(login_frame, text='Login', font=('Arial', 16)).pack(side=TOP)
    Label(login_frame, text='Username:').place(x=20,y=40)
    username_entry = Entry(login_frame)
    username_entry.place(x=90, y=40)
    Label(login_frame, text='Password:').place(x=20, y=80)
    password_entry = Entry(login_frame, show="*")
    password_entry.place(x=90, y=80)
    
    Button(login_frame, text='Login').place(x=90, y=120) 
    Button(login_frame, text='Signup', command=lambda:page_switcher(show_signup(frame,page_switcher))).place(x=150, y=120)
    return login_frame

def show_signup(frame,page_switcher):
    
    signup_frame = ttk.Frame(frame,width=600,height=600)
     
    Button(signup_frame, text='Submit').place(x=130, y=140)
    Button(signup_frame, text='Back to Login', command=lambda:page_switcher(show_login(frame,page_switcher))).place(x=130, y=180)

    Label(signup_frame, text='Sign Up', font=('Arial', 16)).pack(side=TOP)
    Label(signup_frame, text='E-mail:').place(x=20, y=20)
    email_entry = Entry(signup_frame)
    email_entry.place(x=130, y=20)
    Label(signup_frame, text='Username:').place(x=20, y=60)
    new_username_entry = Entry(signup_frame)
    new_username_entry.place(x=130, y=60)
    Label(signup_frame, text='Password:').place(x=20, y=100)
    new_password_entry = Entry(signup_frame, show="*")
    new_password_entry.place(x=130, y=100)
login()