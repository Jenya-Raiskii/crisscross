from tkinter import *
from tkinter import messagebox  
def foo(e):
	i=0
	while i*i<=int(txt.get()):
		i+=1
	i-=1
	print(i*i)
	if i*i==int(txt.get()):
		text["text"]=i
	else:
		text["text"]='Error'
root=Tk()

txt=Entry(root,width=20,font='ArialBlack 17')

text=Label(root,text=' ',font='ArialBlack 17')

root.bind("<Return>", foo)

txt.grid(row=2,column=2)

text.grid(row=3,column=2)

root.mainloop()
