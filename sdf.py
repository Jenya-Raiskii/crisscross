from tkinter import *
from tkinter import messagebox
a ='O'
i=1 
game_count=0
count_check=False
ab=False
def new():
	global i, a
	b=['O','X']
	a = b[i]
	i+=1
	if i==2:
		i=0
	Lab2['text']="Ход: ",a
	return a

def ca(event):
	global a , count_check
	if event.widget['text']==' ':
		event.widget['text']=a
	new()
	reset_on()
def obnul():
	global a
	but1["text"]=' '
	but2["text"]=' '
	but3["text"]=' '
	but4["text"]=' '
	but5["text"]=' '
	but6["text"]=' '
	but7["text"]=' '
	but8["text"]=' '
	but9["text"]=' '

def reset_on():
	global ab, count_check,game_count
	if count_check==True:
		if (but1.cget('text')!= ' ') and but1.cget('text') == but2.cget('text') and but2.cget('text') == but3.cget('text'):
			ab=True
			obnul()
			game_count+=1
			Lab['text']='Игра: ',game_count
		elif (but1.cget('text')!= ' ')and but1.cget('text') == but4.cget('text') and but4.cget('text') == but7.cget('text'):
			ab=True
			obnul()
			game_count+=1
			Lab['text']='Игра: ',game_count
		elif (but4.cget('text')!= ' ')and but4.cget('text') == but5.cget('text') and but5.cget('text') == but6.cget('text'):
			ab=True
			obnul()
			game_count+=1
			Lab['text']='Игра: ',game_count
		elif (but7.cget('text')!= ' ')and but7.cget('text') == but8.cget('text') and but8.cget('text') == but9.cget('text'):
			ab=True
			obnul()
			game_count+=1
			Lab['text']='Игра: ',game_count
		elif (but3.cget('text')!= ' ')and but3.cget('text') == but6.cget('text') and but6.cget('text') == but9.cget('text'):
			ab=True
			obnul()
			game_count+=1
			Lab['text']='Игра: ',game_count
		elif (but2.cget('text')!= ' ')and but2.cget('text') == but5.cget('text') and but5.cget('text') == but8.cget('text'):
			ab=True
			obnul()
			game_count+=1
			Lab['text']='Игра: ',game_count
		elif (but1.cget('text')!= ' ')and but1.cget('text') == but5.cget('text') and but5.cget('text') == but9.cget('text'):
			ab=True
			obnul()
			game_count+=1
			Lab['text']='Игра: ',game_count
		elif (but1.cget('text')!= ' ')and but1.cget('text') == but4.cget('text') and but4.cget('text') == but7.cget('text'):
			ab=True
			obnul()
			game_count+=1
			Lab['text']='Игра: ',game_count
		elif (but3.cget('text')!= ' ')and but3.cget('text') == but5.cget('text') and but5.cget('text') == but7.cget('text'):
			ab=True
			obnul()
			game_count+=1
			Lab['text']='Игра: ',game_count
		return ab

def reset_off(e):	
	global game_count		
	obnul()
	game_count+=1
	Lab['text']='Игра: ',game_count

def cheker_on():
	global count_check, game_count
	messagebox.showinfo(title="Отключено разработчиком", message="Отключено разработчиком")
	count_check=True
def cheker_off():
	global count_check
	messagebox.showinfo(title="АвтоПроверка", message="Успешно выключена")
	count_check=False
	
def exit_root():
	root.destroy()


root=Tk()

root.title("KrissCross")
root.geometry("220x340")

m = Menu(root) 
root.config(menu=m) 
 
auto_cheker = Menu(m, tearoff=0)
auto_cheker.add_command(label="On", command=cheker_on)
auto_cheker.add_command(label="Off",command=cheker_off)
 

m.add_cascade(label="Авто проверка",
                     menu=auto_cheker)
m.add_command(label='Exit', command=exit_root)

but1= Button(root,width=5,height=5,text=' ',font='ArialBlack 9')
but1.bind('<Button-1>',ca)
but2= Button(root,width=5,height=5,text=' ')
but2.bind('<Button-1>',ca)
but3= Button(root,width=5,height=5,text=' ')
but3.bind('<Button-1>',ca)


but4= Button(root,width=5,height=5,text=' ')
but4.bind('<Button-1>',ca)
but5= Button(root,width=5,height=5,text=' ')
but5.bind('<Button-1>',ca)
but6= Button(root,width=5,height=5,text=' ')
but6.bind('<Button-1>',ca)

but7= Button(root,width=5,height=5,text=' ')
but7.bind('<Button-1>',ca)
but8= Button(root,width=5,height=5,text=' ')
but8.bind('<Button-1>',ca)
but9= Button(root,width=5,height=5,text=' ')
but9.bind('<Button-1>',ca)

but_reset= Button(root,width=5,height=5,text='Reset')
but_reset.bind('<Button-1>',reset_off)

Lab=Label(root, width=10,text='Игра: ',font='ArialBlack 10')
Lab2=Label(root, width=10,text='Ход:  ',font='ArialBlack 10')


but1.grid(row=1,column=1)
but2.grid(row=1,column=2)
but3.grid(row=1,column=3)

but4.grid(row=2,column=1)
but5.grid(row=2,column=2)
but6.grid(row=2,column=3)

but7.grid(row=3,column=1)
but8.grid(row=3,column=2)
but9.grid(row=3,column=3)

but_reset.grid(row=5,column=3)

Lab.grid(row=1,column=4)
Lab2.grid(row=2,column=4)


root.mainloop()
