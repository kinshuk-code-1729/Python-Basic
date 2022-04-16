from tkinter import *
root=Tk()
btnRect=Button(root,text="Rectangle",padx=50,pady=10,font=('arial',10,"bold"),bg="cyan",command=lambda:btnClick('Rectangle')).grid(row=1,column=0)
btnCir=Button(root,text="Circle",padx=50,pady=10,font=('arial',10,"bold"),bg="cyan",command=lambda:btnClick('Circle')).grid(row=1,column=1)
btnLine=Button(root,text="Line",padx=50,pady=10,font=('arial',10,"bold"),bg="cyan",command=lambda:btnClick('Line')).grid(row=1,column=2)
def btnClick(n):
    master = Tk()
    w = Canvas(master, width=200, height=100)
    w.pack()
    if n=='Rectangle':
        w.create_rectangle(65, 35, 135, 65, fill="magenta")
    elif n=='Circle':
        w.create_oval(20,20,100,100,fill="light yellow")
    elif n=='Line':
        w.create_line(0, 50, 150, 50, fill="black", width=3)
 
mainloop()
root.mainloop()
