from tkinter import *
from tkinter import messagebox  

def color_red(e):
	txt.delete(0,END)
	txt.insert(0,'Red')
def color_blue(e):
	txt.delete(0,END)
	txt.insert(0,'Blue')
def color_green(e):
	txt.delete(0,END)
	txt.insert(0,'Green')

def new(e):
	text["text"]=txt2.get()

root=Tk()

text=Label(root,width=10,height=1,bg='Brown',text=' ',font='ArialBlack')

f_top=Frame(root,width=120,height=20,bg='Red',bd=10)
f_top.bind("<Button-1>",color_red)

f_body=Frame(root,width=120,height=20,bg='Blue',bd=10)
f_body.bind("<Button-1>",color_blue)

f_down=Frame(root,width=120,height=20,bg='Green',bd=10)
f_down.bind("<Button-1>",color_green)

txt=Entry(root,width=50,bg='Grey',font='ArialBlack')

txt2=Entry(root,width=50,bg='black',font='ArialBlack',fg='White')
txt2.bind("<Return>", new)




text.grid(row=1,column=2)
f_top.grid(row=2,column=2)
f_body.grid(row=3,column=2)
f_down.grid(row=4,column=2)
txt.grid(row=5,column=2)
txt2.grid(row=7,column=2)
root.mainloop()
