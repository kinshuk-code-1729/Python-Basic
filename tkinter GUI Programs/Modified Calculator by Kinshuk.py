import math as m
from tkinter import *

def btnClick(number):
    global operator
    operator=operator+str(number)
    strvar.set(operator)

def btnClear():
    global operator 
    operator=''
    strvar.set(operator)

def result():
    global operator
    
    res=str(eval(operator))
    strvar.set(res)

root=Tk()
root.title("A Graphical & Scientific Calculator")


operator=''

strvar=StringVar()


ent=Entry(width=50,bd=5,font=('Bookman old style',10,"bold"),bg="white",textvariable=strvar,justify="right").grid(columnspan=9)

btn7=Button(text="7",padx=10,pady=10,font=('arial',10,"bold"),bg="cyan",command=lambda:btnClick(7)).grid(row=1,column=0)

btn8=Button(text="8",padx=10,pady=10,font=('arial',10,"bold"),bg="cyan",command=lambda:btnClick(8)).grid(row=1,column=1)

btn9=Button(text="9",padx=10,pady=10,font=('arial',10,"bold"),bg="cyan",command=lambda:btnClick(9)).grid(row=1,column=2)

btnPlus=Button(text="+",padx=10,pady=10,font=('arial',10,"bold"),bg="orange",command=lambda:btnClick('+')).grid(row=1,column=3)

btn4=Button(text="4",padx=10,pady=10,font=('arial',10,"bold"),bg="cyan",command=lambda:btnClick(4)).grid(row=2,column=0)
btn5=Button(text="5",padx=10,pady=10,font=('arial',10,"bold"),bg="cyan",command=lambda:btnClick(5)).grid(row=2,column=1)
btn6=Button(text="6",padx=10,pady=10,font=('arial',10,"bold"),bg="cyan",command=lambda:btnClick(6)).grid(row=2,column=2)
btnMinus=Button(text="-",padx=12,pady=10,font=('arial',10,"bold"),bg="orange",command=lambda:btnClick('-')).grid(row=2,column=3)
btn1=Button(text="1",padx=10,pady=10,font=('arial',10,"bold"),bg="cyan",command=lambda:btnClick(1)).grid(row=3,column=0)
btn2=Button(text="2",padx=10,pady=10,font=('arial',10,"bold"),bg="cyan",command=lambda:btnClick(2)).grid(row=3,column=1)
btn3=Button(text="3",padx=10,pady=10,font=('arial',10,"bold"),bg="cyan",command=lambda:btnClick(3)).grid(row=3,column=2)
btnMulti=Button(text="X",padx=9.5,pady=10,font=('callibri',10),bg="orange",command=lambda:btnClick('*')).grid(row=3,column=3)
btn0=Button(text="0",padx=10,pady=10,font=('arial',10,"bold"),bg="cyan",command=lambda:btnClick(0)).grid(row=4,column=0)
btnClear=Button(text="C",padx=15,pady=15,font=('bookman old style',10,"bold"),bg="red",command=btnClear).grid(row=1,column=5)
btnEqual=Button(text="=",command=result,padx=15,pady=15,font=('arial',10,"bold"),bg="light green").grid(row=4,column=2)
btnDivide=Button(text="÷",padx=12,pady=10,font=('arial',10,"bold"),bg="orange",command=lambda:btnClick('/')).grid(row=4,column=3)
btnPower=Button(text="^",padx=11,pady=10,font=('arial',10,"bold"),bg="orange",command=lambda:btnClick('**')).grid(row=1,column=4)
btnExp=Button(text="e",padx=11,pady=10,font=('arial',10,"bold"),bg="orange",command=lambda:btnClick('m.e')).grid(row=2,column=4)
btnPi=Button(text="π",padx=10,pady=10,font=('arial',10,"bold"),bg="orange",command=lambda:btnClick('m.pi')).grid(row=3,column=4)
btnbrOP=Button(text="(",padx=13,pady=10,font=('arial',10,"bold"),bg="pink",command=lambda:btnClick('(')).grid(row=4,column=6)
btnbrCL=Button(text=")",padx=13,pady=10,font=('arial',10,"bold"),bg="pink",command=lambda:btnClick(')')).grid(row=4,column=7)
btnSqrt=Button(text="√x",padx=7,pady=10,font=('arial',10,"bold italic"),bg="magenta",command=lambda:btnClick('m.sqrt')).grid(row=2,column=5)
btnSq=Button(text="x²",padx=9,pady=10,font=('arial',10,"bold italic"),bg="magenta",command=lambda:btnClick('**2')).grid(row=3,column=5)
btnPoint=Button(text=".",padx=11,pady=10,font=('arial',10,"bold"),bg="cyan",command=lambda:btnClick('.')).grid(row=4,column=1)
btnsin=Button(text="sin",padx=6,pady=10,font=('arial',10,"bold"),bg="powder blue",command=lambda:btnClick('m.sin')).grid(row=1,column=6)
btncos=Button(text="cos",padx=4.5,pady=10,font=('arial',10,"bold"),bg="powder blue",command=lambda:btnClick('m.cos')).grid(row=2,column=6)
btntan=Button(text="tan",padx=5,pady=10,font=('arial',10,"bold"),bg="powder blue",command=lambda:btnClick('m.tan')).grid(row=3,column=6)
btnfact=Button(text="n!",padx=9,pady=10,font=('arial',10,"bold"),bg="orange",command=lambda:btnClick('m.factorial')).grid(row=4,column=4)
btnabs=Button(text="| x |",padx=8,pady=10,font=('arial',10,"bold italic"),bg="magenta",command=lambda:btnClick('m.fabs')).grid(row=4,column=5)
btnf2=Button(text="1 ⁄ x",padx=10,pady=10,font=('arial',10,"bold italic"),bg="pink",command=lambda:btnClick('**(-1)')).grid(row=1,column=7)
btndeg=Button(text="deg.",padx=3,pady=10,font=('arial',10,"bold"),bg="blue",command=lambda:btnClick('m.degrees')).grid(row=2,column=7)
btnrad=Button(text="rad.",padx=3,pady=10,font=('arial',10,"bold"),bg="blue",command=lambda:btnClick('m.radians')).grid(row=3,column=7)
btnlogn=Button(text="ln",padx=10,pady=10,font=('arial',10,"bold italic"),bg="light yellow",command=lambda:btnClick('m.log')).grid(row=1,column=8)
btnlog10=Button(text="log",padx=6,pady=10,font=('arial',10,"bold"),bg="light yellow",command=lambda:btnClick('m.log10')).grid(row=2,column=8)
btnexp=Button(text="exp",padx=4,pady=10,font=('arial',10,"bold"),bg="light yellow",command=lambda:btnClick('m.exp')).grid(row=3,column=8)
btnper=Button(text="%",padx=10,pady=10,font=('arial',10,"bold"),bg="light yellow",command=lambda:btnClick('/100')).grid(row=4,column=8)
Label().grid(row=5,columnspan=4)
Label(text="CREATED & DESIGNED BY -- Kinshuk Banerjee",font=('Bookman Old Style',10,'bold'),fg='black',bg='white').grid(row=6,columnspan=8)
root.mainloop()
