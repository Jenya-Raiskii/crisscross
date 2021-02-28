from tkinter import *
from tkinter import messagebox  
root=Tk()
#Список(Listbox)
"""r = ['python','tk','linux']
lst_tk=Listbox(root,selectmode=EXTENDED,height=4)
for i in r:
	lst_tk.insert(END,i)
#inser(index,elem)-вставляет elem на index; END - вставить в конец
lst_tk.pack()"""
'''
selectmode - сколько эл-ов можно выбрать
height - сколько эл-ов списка отображаются на экране
'''
#Рамка (Frame)
fra = Frame(root,width=300,height=100,bg='Green',bd=20)
fra2 = Frame(root,width=300,height=100,bg='DarkGreen',bd=20)
txt=Entry(fra2,width=20)
#Шкала (Scale)
sca1=Scale(fra,orient=HORIZONTAL, length=300,from_=0,to=100,tickinterval=10,resolution=5)
fra.pack()
sca1.pack()
fra2.pack()
txt.pack()

'''
orient - ориентация (HORIZONTAL, VERTICAL)
length - длина шкалы в пикселях
from_ откуда начнётся шкала
to - на каком значении шкала заканчивается
tickinterval - расстояние между засечками на шкале
resolution - на сколько можно двигать ползунок
'''
#Окно верхнего уровня(Toplevel)
root.mainloop()
"""
root=Tk()
txt1=Label(root,text='Hello')
win1=Toplevel(root)
txt2=Label(win1,text='World')
win2=Toplevel(root)
txt=Entry(win2,width=20)
txt1.pack()
txt2.pack()
txt.pack()
"""