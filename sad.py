from tkinter import *
from tkinter import messagebox  

def foo(e):
	text["text"]=txt.get(1.0,END)

root=Tk()

text=Label(root,text=' ',font='ArialBlack 17')

txt=Text(root,width=20,height=4,font='ArialBlack 17')

root.bind("<Return>",foo)

text.grid(row=1,column=2)
txt.grid(row=2,column=2)

root.mainloop()
