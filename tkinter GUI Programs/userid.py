from tkinter import *
from tkinter import messagebox

def passwd_verify(pswd):

    if pswd=="ashok1969#":
        messagebox.showinfo("Password Verified !!!","Correct Password..")
    else:
        messagebox.showinfo("Password Not Verified ###","Wrong Password..")

root=Tk()
root.geometry("400x250")
root.title("Login Form")
name=Label(root,text="User ID").place(x=30,y=50)
email=Label(root,text="Email").place(x=30,y=90)
password=Label(root,text="Password").place(x=30,y=140)

e1=Entry(root).place(x=90,y=50)
e2=Entry(root)
e2.place(x=90,y=90)
e3=Entry(root,show="*")
e3.place(x=90,y=130)

sub=Button(root,text="Submit",padx=30,pady=10,font=('Bookman old style',15,"bold"),bg="cyan",command=lambda:passwd_verify(e3.get()))
sub.place(bordermode=OUTSIDE,height=30,width=80,x=90,y=170)
root.mainloop()
