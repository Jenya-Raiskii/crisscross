from tkinter import *
from tkinter import messagebox  

def plus(event):
	fra['width']+=10
	fra['height']+=10
def minus(event):
	if fra['width']==10:
	   messagebox.showinfo('Error', 'Error')  
	else:
		fra['width']-=10
		fra['height']-=10

root=Tk()
fra = Frame(root,width=20,height=20,bg='Green',bd=20)
but_purple = Button(root, bg="purple", text='Увеличить')
but_purple.bind('<Button-1>',plus)
but_gray = Button(root, bg="gray", text='Уменьшить')
but_gray.bind('<Button-1>',minus)
fra.pack()
but_purple.pack()
but_gray.pack()
root.mainloop()
