from tkinter import *
from tkinter import messagebox  
color = "Red"
i = 0
d=1
def rr(event):
	if c == True:
	    txt3.insert(0,a+b)
	    txt.delete(0,END)
	    txt2.delete(0,END)
	else:
		print('Error') 

def save(event):
	global a, b ,c
	a=txt.get()
	b=txt2.get()
	c = False
	for i in a:
		if i == "0" or i == "1" or i == "2" or i == "3" or i == "4" or i == "5" or i == "6" or i == "7" or i == "8" or i == "9":
			c = True
		else:
			c = False
	if c == True:
		a = int(a)
	if c == True:
		c=False
		for i in b:
			if i == "0" or i == "1" or i == "2" or i == "3" or i == "4" or i == "5" or i == "6" or i == "7" or i == "8" or i == "9":
				c = True
			else:
				c = False
	if c == True:
		b = int(b)
	txt3.delete(0,END)

def mas(event):
	global a, b
	if c==True:
		txt3.insert(0,a/b)
		txt.delete(0,END)
		txt2.delete(0,END)
	else:
		print('Error')

def ff(event):  
	if c==True:
		txt3.insert(0,a**b)
		txt.delete(0,END)
		txt2.delete(0,END)
	else:
		print('Error')

root = Tk()
root.geometry("480x480")
but = Button(root, bg=color, text='+')
but.bind('<Button-1>', rr)
but_purple = Button(root, bg="purple", text='**')
but_purple.bind('<Button-1>',ff)
but_gray = Button(root, bg="gray", text='/')
but_gray.bind('<Button-1>',mas)
txt=Entry(root,width=10,text='Number one')
txt2=Entry(root,width=10,text='Number two')
but_pink = Button(root, bg="pink", text='Save')
but_pink.bind('<Button-1>', save)
txt3=Entry(root,width=10,text=d)
but.pack()
but_purple.pack()
but_gray.pack()
txt.pack()
txt2.pack()
but_pink.pack()
txt3.pack()

root.mainloop()
