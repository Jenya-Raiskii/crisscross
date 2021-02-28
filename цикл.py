from tkinter import *
from tkinter import messagebox
def cikl(e):
	a = ['adas','akd','ajd','adg','adf','add','ads',1,232,23,35,25]
	for z in a:		
		text['text']=z

root=Tk()

text=Label(width=40,text=' ')

btn=Button(root,width=5,height=5,bg='Green')
btn.bind('<Button-1>', cikl)

text.pack()

btn.pack()

root.mainloop()
