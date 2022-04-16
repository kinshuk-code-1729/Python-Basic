from tkinter import *
import tkinter

top = Tk()

mb = Menubutton(top, text="MENUS", relief=RAISED)
mb.grid()
mb.menu = Menu(mb, tearoff = 0)
mb["menu"] = mb.menu

v1 = IntVar()
v2 = IntVar()

mb.menu.add_checkbutton(label="New",variable=v1)
mb.menu.add_checkbutton(label="Open",variable=v2)

mb.pack()
top.mainloop()
