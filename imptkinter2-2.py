from tkinter import *
import sqlite3
from tkinter import messagebox

root = Tk()
root.geometry("500x650")

conn=sqlite3.connect("Customer_registration.db")
c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS registration (
           full_name VARCHAR(20),
           phone CHAR(10),
           email VARCHAR(30),
           address VARCHAR(30))""")
conn.commit()
conn.close()

def add():
    f=full_name.get()
    p=phone.get()
    e=email.get()
    a=address.get()
    if not f or not p or not e or not a:
        messagebox.showerror("Error", "Please fill all fields")
        return

    conn=sqlite3.connect("Customer_registration.db")
    c = conn.cursor()
    c.execute('INSERT INTO registration (full_name,phone,email,address) values("{}","{}","{}","{}")'.format(f,p,e,a))
    conn.commit()
    conn.close()
    full_name.delete(0,END)
    phone.delete(0,END)
    email.delete(0,END)
    address.delete(0,END)
    
def get_customer_details():
    conn=sqlite3.connect('Customer_registration.db')
    c=conn.cursor()
    c.execute('SELECT *,oid FROM registration where address="boudha"')
    records=c.fetchall()
    conn.close()
    printed_records=''
    for i in records:
        printed_records=printed_records+i[0]+' '+i[2]+' '+str(i[4]) +"\n"
    show_record.config(text=printed_records)
    
def delete_records():
    oid=delete_record.get()
    if not oid:
        messagebox.showerror("Error","please enter a ID")
        return
    
    conn =sqlite3.connect('Customer_registration.db')
    c=conn.cursor()
    c.execute('DELETE FROM registration WHERE oid=?',(delete_record.get(),))
    conn.commit()
    conn.close()
    
    delete_record.delete(0,END)
    get_customer_details()

def edit_details():
    if not delete_record.get():
        messagebox.showerror("Error","please enter a ID")
        return
    def update():
        f=full_name.get()
        p=phone.get()
        e=email.get()
        a=address.get()
        
        conn=sqlite3.connect('Customer_registration.db')
        c=conn.cursor()
        c.execute('''
                  UPDATE registration SET full_name=?,phone=?,email=?,address=? WHERE oid=?
                  ''',(f,p,e,a,))   # f , p, etc are gone to=? respectively
        conn.commit()
        conn.close()
        messagebox.showinfo('Sucess','Record updated sucessfully')
        editor.destroy()        
    
    editor=Toplevel()
    editor.configure(bg="white")
    editor.title('Update records') 
    editor.geometry('500x500') 

    lbl_fullname=Label(editor,text="Fullname",bg="white",font=("arial",12))
    lbl_fullname.place(x=50,y=80)
    full_name=Entry(editor,width=35,font=("arial",11))
    full_name.place(x=180,y=80)
    lbl_phone=Label(editor,text="Phone",bg="white",font=("arial",12))
    lbl_phone.place(x=50,y=130)
    phone=Entry(editor,width=35,font=("arial",11))
    phone.place(x=180,y=130)

    lbl_email=Label(editor,text="Email",bg="white",font=("arial",12))
    lbl_email.place(x=50,y=180)
    email=Entry(editor,width=35,font=("arial",11))
    email.place(x=180,y=180)
    
    lbl_address=Label(editor,text="Address",bg="white",font=("arial",12))
    lbl_address.place(x=50,y=230)
    address=Entry(editor,width=35,font=("arial",11))
    address.place(x=180,y=230)
    
    btn_register=Button(editor,text="Save",bg="green",fg="white",font=("arial",11,"bold"),command=update)
    btn_register.place(x=200,y=280)
    
    conn=sqlite3.connect('Customer_registration.db')
    c=conn.cursor()
    c.execute('SELECT * FROM registration where oid=?',(delete_record.get(),))
    records=c.fetchall()
    
    for record in records:
        full_name.insert(0,record[0])
        phone.insert(0,record[1])
        email.insert(0,record[2])
        address.insert(0,record[3])
    conn.commit()    
    conn.close()
        

   

llb_registration=Label(root,text="Customer_Registration Form",
                       font=("arial",16,"bold"),
                       bg="white",fg="darkblue")
llb_registration.place(x=120,y=20)

lbl_fullname=Label(root,text="Fullname",bg="white",font=("arial",12))
lbl_fullname.place(x=50,y=80)
full_name=Entry(root,width=35,font=("arial",11))
full_name.place(x=180,y=80)


lbl_phone=Label(root,text="Phone",bg="white",font=("arial",12))
lbl_phone.place(x=50,y=130)
phone=Entry(root,width=35,font=("arial",11))
phone.place(x=180,y=130)

lbl_email=Label(root,text="Email",bg="white",font=("arial",12))
lbl_email.place(x=50,y=180)
email=Entry(root,width=35,font=("arial",11))
email.place(x=180,y=180)

lbl_address=Label(root,text="Address",bg="white",font=("arial",12))
lbl_address.place(x=50,y=230)
address=Entry(root,width=35,font=("arial",11))
address.place(x=180,y=230)


btn_register=Button(root,text="Register",bg="green",fg="white",font=("arial",11,"bold"),command=add)
btn_register.place(x=200,y=280)

btn_fetch=Button(root,text="show records",bg="blue",fg="white",font=("arial",11,"bold"),command=get_customer_details)
btn_fetch.place(x=190,y=330)


lbl_delete=Label(root,text="Enter Id Delete",bg="white",font=("arial",11))
lbl_delete.place(x=50,y=380)

delete_record=Entry(root,width=20,font=("arial",11))
delete_record.place(x=200,y=380)

btn_delete=Button(root,text="Delete",bg="red",fg="white",font=("arial",11,"bold"),command=delete_records)
btn_delete.place(x=380,y=375)

btn_edit=Button(root,text="Edit",bg="green",fg="white",font=("arial",11,"bold"),command=edit_details)
btn_edit.place(x=450,y=375)


show_record=Label(root,text="Show Records",bg="white",justify="right",anchor="nw",font=("Courier",11),relief=SOLID,width=35,height=15)
show_record.place(x=30,y=430)
root.mainloop()