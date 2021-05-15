import telebot
import csv
from telebot import types
from random import *
bot = telebot.TeleBot("1885186106:AAFK-lXLmBngO9K3OHI0FJoVZMWxaJFO01g")
@bot.message_handler(commands=['help', 'start'])
def start_message(message):
   	bot.send_message(message.chat.id, 'Привет, пропиши /about, чтобы узнать обо мне.👍')
   	your_variable = [[str(message.from_user.id)]]
   	key=[]
   	print(your_variable)
   	with open('bd.scv','r') as bd:
   		reader = csv.reader(bd)
   		for row in reader:
   			key.append(row)
   			if your_variable in key:
   				print(1)
   			else:
   				with open('bd.scv','a') as bd:
   					writer = csv.writer(bd)
   					writer.writerows(your_variable)
@bot.message_handler(commands=['about'])
def about_me(message):
	bot.send_message(message.chat.id,'''
⭐️Привет, создателя бота зовут Женя.
🌈Телеграмм - @ykculneo
⭐️Запросить гдз - /gdz
🌈Игра - /game
⭐️Музыка для выполнения работы - /music
		''')
@bot.message_handler(commands=['music'])
def music_every_week(message):
	bot.send_message(message.chat.id,'Слушай музыку и кайфуй😎')
	p = open('pic_01.gif',"rb")
	bot.send_animation(message.chat.id,p)
	bot.send_audio(message.chat.id,open('music_01.mp3','rb'))
	bot.send_audio(message.chat.id,open('music_02.mp3','rb'))
	bot.send_audio(message.chat.id,open('music_03.mp3','rb'))
	bot.send_audio(message.chat.id,open('music_04.mp3','rb'))
	bot.send_audio(message.chat.id,open('music_05.mp3','rb'))
@bot.message_handler(commands=['game'])
def nvuti_game(message):
	markup_inline= types.InlineKeyboardMarkup()
	m0 = types.InlineKeyboardButton(text='Меньше',callback_data='men0')
	b0 = types.InlineKeyboardButton(text='Больше',callback_data='bol0')
	markup_inline.add(m0,b0)
	bot.send_message(message.chat.id,'''❗️Игра пока что одна, но поиграть можно
❗️В данной игре тебе нужно угадать какое число сейчас выпадет.
❗️Сделать это можно путём нажатия на кноку.
❗️Больше или меньше.
		''',reply_markup=markup_inline)
@bot.callback_query_handler(func = lambda call: True)
def proverka(call):
	random_num = randint(0,10000)
	item_back=types.InlineKeyboardButton(text='Вернуться',callback_data='back')
	if call.data=="men0":
		if random_num<5000:
			markup_inline= types.InlineKeyboardMarkup()
			m0 = types.InlineKeyboardButton(text='Меньше',callback_data='men0')
			b0 = types.InlineKeyboardButton(text='Больше',callback_data='bol0')
			markup_inline.add(m0,b0)
			bot.send_message(call.message.chat.id,'Ты выиграл, число:'+str(random_num),reply_markup=markup_inline)
			bot.send_photo(call.message.chat.id,open('like.png','rb'))
		else:
			markup_inline= types.InlineKeyboardMarkup()
			m0 = types.InlineKeyboardButton(text='Меньше',callback_data='men0')
			b0 = types.InlineKeyboardButton(text='Больше',callback_data='bol0')
			markup_inline.add(m0,b0)
			bot.send_message(call.message.chat.id,'Ты проиграл, число:'+str(random_num),reply_markup=markup_inline)
			bot.send_photo(call.message.chat.id,open('diz.png','rb'))
	elif call.data=='bol0':
		if random_num>5000:
			markup_inline= types.InlineKeyboardMarkup()
			m0 = types.InlineKeyboardButton(text='Меньше',callback_data='men0')
			b0 = types.InlineKeyboardButton(text='Больше',callback_data='bol0')
			markup_inline.add(m0,b0)
			bot.send_message(call.message.chat.id,'Ты выиграл, число:'+str(random_num),reply_markup=markup_inline)
			bot.send_photo(call.message.chat.id,open('like.png','rb'))
		else:
			markup_inline= types.InlineKeyboardMarkup()
			m0 = types.InlineKeyboardButton(text='Меньше',callback_data='men0')
			b0 = types.InlineKeyboardButton(text='Больше',callback_data='bol0')
			markup_inline.add(m0,b0)
			bot.send_message(call.message.chat.id,'Ты проиграл, число:'+str(random_num),reply_markup=markup_inline)
			bot.send_photo(call.message.chat.id,open('diz.png','rb'))
	elif call.data=="pizda":
		markup_reply= types.ReplyKeyboardMarkup(resize_keyboard= True)
		item_back=types.KeyboardButton(text='Вернуться')
		markup_reply.add(item_back)
		bot.send_message(call.message.chat.id,'20 числа итоговая контрольная работа по обществознанию, если найду ответы, то они будут здесь, а если нет, то нам будет плохо',reply_markup=markup_reply)
	elif call.data == "a":
		markup_inline=types.InlineKeyboardMarkup()
		back=types.InlineKeyboardButton(text='Вернуться',callback_data='back')
		xim=types.InlineKeyboardButton(text='Химия',callback_data='a_xim')
		fiz=types.InlineKeyboardButton(text='Физика',callback_data='a_fiz')
		bio=types.InlineKeyboardButton(text='Биология',callback_data='a_bio')
		nem=types.InlineKeyboardButton(text='Немецкий',callback_data='a_nem')
		rus=types.InlineKeyboardButton(text='Русский',callback_data='a_rus')
		geom=types.InlineKeyboardButton(text='Геометрия',callback_data='a_geom')
		lit=types.InlineKeyboardButton(text='Литература',callback_data='a_lit')
		markup_inline.add(xim,fiz,bio,nem,rus,geom,lit,back)
		bot.send_message(call.message.chat.id,'Выбирай предмет',reply_markup=markup_inline)
	elif call.data == "b":
		markup_inline=types.InlineKeyboardMarkup()
		back=types.InlineKeyboardButton(text='Вернуться',callback_data='back')
		xim=types.InlineKeyboardButton(text='Русский',callback_data='b_rus')
		fiz=types.InlineKeyboardButton(text='Физика',callback_data='b_fiz')
		bio=types.InlineKeyboardButton(text='Алгебра',callback_data='b_arg')
		nem=types.InlineKeyboardButton(text='Англиский',callback_data='b_eng')
		rus=types.InlineKeyboardButton(text='Информатика',callback_data='b_inf')
		geom=types.InlineKeyboardButton(text='Физкультура',callback_data='b_fizk')
		markup_inline.add(xim,fiz,bio,nem,rus,geom,back)
		bot.send_message(call.message.chat.id,'Выбирай предмет',reply_markup=markup_inline)
	elif call.data == "c":
		p = open("dz_01.jpg","rb")
		bot.send_photo(call.message.chat.id,p)
		bot.send_message(call.message.chat.id,'На этот день ничего не задано.')
	elif call.data == "d":
		p = open("dz_01.jpg","rb")
		bot.send_photo(call.message.chat.id,p)
		bot.send_message(call.message.chat.id,'На этот день ничего не задано.')
	elif call.data == "e":
		p = open("dz_01.jpg","rb")
		bot.send_photo(call.message.chat.id,p)
		bot.send_message(call.message.chat.id,'На этот день ничего не задано.')
	elif call.data == "f":
		bot.send_photo(call.message.chat.id,open("dz_01.jpg","rb"))
		bot.send_message(call.message.chat.id,'На этот день ничего не задано.')
	elif call.data=='a_xim':
		markup_inline=types.InlineKeyboardMarkup()
		back=types.InlineKeyboardButton(text='Вернуться',callback_data='back_a')
		markup_inline.add(back)
		bot.send_message(call.message.chat.id,'''На этот день заданно повторить теорию и подготовится к КР.
		Теория ниже ⬇️⬇️⬇️
			''')
		bot.send_photo(call.message.chat.id,open("gdz/a_01.jpg","rb"))
		bot.send_photo(call.message.chat.id,open("gdz/a_02.jpg","rb"))
		bot.send_photo(call.message.chat.id,open("gdz/a_03.jpg","rb"))
		bot.send_photo(call.message.chat.id,open("gdz/a_04.jpg","rb"))
		bot.send_photo(call.message.chat.id,open("gdz/a_05.jpg","rb"))
		bot.send_photo(call.message.chat.id,open("gdz/a_06.jpg","rb"))
		bot.send_photo(call.message.chat.id,open("gdz/a_07.jpg","rb"))
		bot.send_photo(call.message.chat.id,open("gdz/a_08.jpg","rb"))
		bot.send_photo(call.message.chat.id,open("gdz/a_09.jpg","rb"))
		bot.send_message(call.message.chat.id,'Вернуться',reply_markup=markup_inline)
	elif call.data=='a_fiz':
		markup_inline=types.InlineKeyboardMarkup()
		back=types.InlineKeyboardButton(text='Вернуться',callback_data='back_a')
		markup_inline.add(back)
		bot.send_message(call.message.chat.id,'На этот день заданно повторить п.63')
		bot.send_message(call.message.chat.id,'Вернуться',reply_markup=markup_inline)
	elif call.data=='a_bio':
		markup_inline=types.InlineKeyboardMarkup()
		back=types.InlineKeyboardButton(text='Вернуться',callback_data='back_a')
		markup_inline.add(back)
		bot.send_message(call.message.chat.id,'На этот день заданно повторить п.49')
		bot.send_message(call.message.chat.id,'Вернуться',reply_markup=markup_inline)
	elif call.data=='a_nem':
		markup_inline=types.InlineKeyboardMarkup()
		back=types.InlineKeyboardButton(text='Вернуться',callback_data='back_a')
		markup_inline.add(back)
		bot.send_message(call.message.chat.id,'На этот день ничего не заданно')
		bot.send_message(call.message.chat.id,'Вернуться',reply_markup=markup_inline)
	elif call.data=='a_rus':
		markup_inline=types.InlineKeyboardMarkup()
		back=types.InlineKeyboardButton(text='Вернуться',callback_data='back_a')
		markup_inline.add(back)
		bot.send_message(call.message.chat.id,'''На этот день заданно подготовиться к огэ и "ЯКЛАСС"
		Т.к заданн "ЯКЛАСС", ответов не будет.
			''')
		bot.send_message(call.message.chat.id,'Вернуться',reply_markup=markup_inline)
	elif call.data=='a_geom':
		markup_inline=types.InlineKeyboardMarkup()
		back=types.InlineKeyboardButton(text='Вернуться',callback_data='back_a')
		markup_inline.add(back)
		bot.send_message(call.message.chat.id,'''На этот день заданно подготовиться к огэ и "ЯКЛАСС"
		Т.к заданн "ЯКЛАСС", ответов не будет.
			''')
		bot.send_message(call.message.chat.id,'Вернуться',reply_markup=markup_inline)
	elif call.data=='a_lit':
		markup_inline=types.InlineKeyboardMarkup()
		back=types.InlineKeyboardButton(text='Вернуться',callback_data='back_a')
		markup_inline.add(back)
		bot.send_message(call.message.chat.id,'На этот день заданно прочитать пьесу Шекспира "Гамлет"')
		bot.send_message(call.message.chat.id,'Краткое содержание - https://obrazovaka.ru/books/shekspir/gamlet"')
		bot.send_message(call.message.chat.id,'Вернуться',reply_markup=markup_inline)	
	elif call.data=='back_a':
		markup_inline=types.InlineKeyboardMarkup()
		xim=types.InlineKeyboardButton(text='Химия',callback_data='a_xim')
		fiz=types.InlineKeyboardButton(text='Физика',callback_data='a_fiz')
		bio=types.InlineKeyboardButton(text='Биология',callback_data='a_bio')
		nem=types.InlineKeyboardButton(text='Немецкий',callback_data='a_nem')
		rus=types.InlineKeyboardButton(text='Русский',callback_data='a_rus')
		geom=types.InlineKeyboardButton(text='Геометрия',callback_data='a_geom')
		lit=types.InlineKeyboardButton(text='Литература',callback_data='a_lit')
		back=types.InlineKeyboardButton(text='Вернуться',callback_data='back')
		markup_inline.add(xim,fiz,bio,nem,rus,geom,lit,back)
		bot.send_message(call.message.chat.id,'Выбирай предмет',reply_markup=markup_inline)
	elif call.data=='back_b':
		markup_inline=types.InlineKeyboardMarkup()
		back=types.InlineKeyboardButton(text='Вернуться',callback_data='back')
		xim=types.InlineKeyboardButton(text='Русский',callback_data='b_rus')
		fiz=types.InlineKeyboardButton(text='Физика',callback_data='b_fiz')
		bio=types.InlineKeyboardButton(text='Алгебра',callback_data='b_arg')
		nem=types.InlineKeyboardButton(text='Англиский',callback_data='b_eng')
		rus=types.InlineKeyboardButton(text='Информатика',callback_data='b_inf')
		geom=types.InlineKeyboardButton(text='Физкультура',callback_data='b_fizk')
		markup_inline.add(xim,fiz,bio,nem,rus,geom,back)
		bot.send_message(call.message.chat.id,'Выбирай предмет',reply_markup=markup_inline)
	elif call.data=='back_c':
		markup_inline=types.InlineKeyboardMarkup()
		back=types.InlineKeyboardButton(text='Вернуться',callback_data='back')
		xim=types.InlineKeyboardButton(text='Физика',callback_data='c_fizk')
		fiz=types.InlineKeyboardButton(text='Немецкий',callback_data='b_nem')
		bio=types.InlineKeyboardButton(text='Химия',callback_data='c_xim')
		nem=types.InlineKeyboardButton(text='География',callback_data='c_geog')
		rus=types.InlineKeyboardButton(text='Геометрия',callback_data='c_geom')
		geom=types.InlineKeyboardButton(text='Физкультура',callback_data='cb_fizk')
		lit=types.InlineKeyboardButton(text='Литература',callback_data='c_lit')
		markup_inline.add(xim,fiz,bio,nem,rus,geom,back)
		bot.send_message(call.message.chat.id,'Выбирай предмет',reply_markup=markup_inline)
		
	elif call.data=='back':
		markup_inline= types.InlineKeyboardMarkup()
		item_1=types.InlineKeyboardButton(text='ДЗ на 11.05',callback_data='a')
		item_2=types.InlineKeyboardButton(text='ДЗ на 12.05',callback_data='b')
		item_3=types.InlineKeyboardButton(text='ДЗ на 13.05',callback_data='c')
		item_4=types.InlineKeyboardButton(text='ДЗ на 14.05',callback_data='d')
		item_5=types.InlineKeyboardButton(text='ДЗ на 17.05',callback_data='e')
		item_6=types.InlineKeyboardButton(text='ДЗ на 18.05',callback_data='f')
		item_7=types.InlineKeyboardButton(text='Что будет 20.05.2021',callback_data='pizda')
		markup_inline.add(item_1,item_2,item_3,item_4,item_5,item_6,item_7)
		bot.send_message(call.message.chat.id,'Гдз на ближайщие работы',reply_markup=markup_inline)
	elif call.data=='b_rus':
		markup_inline=types.InlineKeyboardMarkup()
		back=types.InlineKeyboardButton(text='Вернуться',callback_data='back_b')
		markup_inline.add(back)
		bot.send_message(call.message.chat.id,'''На этот день заданно Упр.453 и выполнить работу в "ЯКЛАСС", для тех кто не выполнил.
		Ответ на Упр.453 ⬇️⬇️⬇️
			''')
		bot.send_photo(call.message.chat.id,open("gdz/a_10.jpg","rb"))
		bot.send_message(call.message.chat.id,'Вернуться',reply_markup=markup_inline)
	elif call.data=='b_fiz':
		markup_inline=types.InlineKeyboardMarkup()
		back=types.InlineKeyboardButton(text='Вернуться',callback_data='back_b')
		markup_inline.add(back)
		bot.send_message(call.message.chat.id,'''На этот день заданно п.63, повторить формулы.
			Теория ниже ⬇️⬇️⬇️
			''')
		bot.send_photo(call.message.chat.id,open("gdz/b_01.jpg","rb"))
		bot.send_photo(call.message.chat.id,open("gdz/b_02.jpg","rb"))
		bot.send_photo(call.message.chat.id,open("gdz/b_03.jpg","rb"))
		bot.send_photo(call.message.chat.id,open("gdz/b_04.jpg","rb"))
		bot.send_photo(call.message.chat.id,open("gdz/b_05.jpg","rb"))
		bot.send_photo(call.message.chat.id,open("gdz/b_06.jpg","rb"))
		bot.send_photo(call.message.chat.id,open("gdz/b_07.jpg","rb"))
		bot.send_photo(call.message.chat.id,open("gdz/b_08.jpg","rb"))
		bot.send_photo(call.message.chat.id,open("gdz/b_09.jpg","rb"))
		bot.send_photo(call.message.chat.id,open("gdz/b_10.jpg","rb"))
		bot.send_photo(call.message.chat.id,open("gdz/b_11.jpg","rb"))
	elif call.data=='b_arg':
		markup_inline=types.InlineKeyboardMarkup()
		back=types.InlineKeyboardButton(text='Вернуться',callback_data='back_b')
		markup_inline.add(back)
		bot.send_message(call.message.chat.id,'''На этот день заданн "ЯКЛАСС"
		Т.к заданн "ЯКЛАСС", ответов не будет.
			''')
		bot.send_message(call.message.chat.id,'Вернуться',reply_markup=markup_inline)	
	elif call.data == 'b_eng':
		markup_inline=types.InlineKeyboardMarkup()
		back=types.InlineKeyboardButton(text='Вернуться',callback_data='back_b')
		markup_inline.add(back)
		bot.send_message(call.message.chat.id,'''На этот день заданно повторение.
			''')
		bot.send_message(call.message.chat.id,'Вернуться',reply_markup=markup_inline)
	elif call.data == 'b_inf':
		markup_inline=types.InlineKeyboardMarkup()
		back=types.InlineKeyboardButton(text='Вернуться',callback_data='back_b')
		markup_inline.add(back)
		bot.send_message(call.message.chat.id,'''На этот день заданно ничего 😁.
			''')
		bot.send_message(call.message.chat.id,'Вернуться',reply_markup=markup_inline)
	elif call.data =='b_fizk':
		markup_inline=types.InlineKeyboardMarkup()
		back=types.InlineKeyboardButton(text='Вернуться',callback_data='back_b')
		markup_inline.add(back)
		bot.send_message(call.message.chat.id,'''На этот день заданно "Комплекс ОРУ" 😁.
			''')
		bot.send_message(call.message.chat.id,'Вернуться',reply_markup=markup_inline)		
	elif call.data == 'c_fiz':
		markup_inline=types.InlineKeyboardMarkup()
		back=types.InlineKeyboardButton(text='Вернуться',callback_data='back_b')
		markup_inline.add(back)
		bot.send_message(call.message.chat.id,'''На этот день заданно п.63, повторить формулы.
			Теория ниже ⬇️⬇️⬇️
			''')
		bot.send_photo(call.message.chat.id,open("gdz/b_01.jpg","rb"))
		bot.send_photo(call.message.chat.id,open("gdz/b_02.jpg","rb"))
		bot.send_photo(call.message.chat.id,open("gdz/b_03.jpg","rb"))
		bot.send_photo(call.message.chat.id,open("gdz/b_04.jpg","rb"))
		bot.send_photo(call.message.chat.id,open("gdz/b_05.jpg","rb"))
		bot.send_photo(call.message.chat.id,open("gdz/b_06.jpg","rb"))
		bot.send_photo(call.message.chat.id,open("gdz/b_07.jpg","rb"))
		bot.send_photo(call.message.chat.id,open("gdz/b_08.jpg","rb"))
		bot.send_photo(call.message.chat.id,open("gdz/b_09.jpg","rb"))
		bot.send_photo(call.message.chat.id,open("gdz/b_10.jpg","rb"))
		bot.send_photo(call.message.chat.id,open("gdz/b_11.jpg","rb"))
		bot.send_message(call.message.chat.id,'Вернуться',reply_markup=markup_inline)
	elif call.data == 'c_nem':
		markup_inline=types.InlineKeyboardMarkup()
		back=types.InlineKeyboardButton(text='Вернуться',callback_data='back_b')
		markup_inline.add(back)
		bot.send_message(call.message.chat.id,'''На этот день заданно ничего 😁.
			''')
		bot.send_message(call.message.chat.id,'Вернуться',reply_markup=markup_inline)
	elif call.data =='b_xim':
		markup_inline=types.InlineKeyboardMarkup()
		back=types.InlineKeyboardButton(text='Вернуться',callback_data='back_b')
		markup_inline.add(back)
		bot.send_message(call.message.chat.id,'''На этот день заданно "Повторить строение атома углерода".
			''')
		bot.send_message(call.message.chat.id,'Вернуться',reply_markup=markup_inline)		
	elif call.data == 'c_geor':
		markup_inline=types.InlineKeyboardMarkup()
		back=types.InlineKeyboardButton(text='Вернуться',callback_data='back_b')
		markup_inline.add(back)
		bot.send_message(call.message.chat.id,'''На этот день заданно повторение.
			''')
		bot.send_message(call.message.chat.id,'Вернуться',reply_markup=markup_inline)
	elif call.data == 'c_geom':
		markup_inline=types.InlineKeyboardMarkup()
		back=types.InlineKeyboardButton(text='Вернуться',callback_data='back_b')
		markup_inline.add(back)
		bot.send_message(call.message.chat.id,'''На этот день заданно задание в файле.
			Ответы ниже ⬇️⬇️⬇️
			''')
		bot.send_photo(call.message.chat.id,open("gdz/b_01.jpg","rb"))
		bot.send_message(call.message.chat.id,'Вернуться',reply_markup=markup_inline)
	elif call.data =='c_fizk':
		markup_inline=types.InlineKeyboardMarkup()
		back=types.InlineKeyboardButton(text='Вернуться',callback_data='back_b')
		markup_inline.add(back)
		bot.send_message(call.message.chat.id,'''На этот день заданно "Комплекс ОРУ" 😁.
			''')
		bot.send_message(call.message.chat.id,'Вернуться',reply_markup=markup_inline)		
	
	elif call.data=='c_lit':
		markup_inline=types.InlineKeyboardMarkup()
		back=types.InlineKeyboardButton(text='Вернуться',callback_data='back_a')
		markup_inline.add(back)
		bot.send_message(call.message.chat.id,'На этот день заданно прочитать пьесу Шекспира "Гамлет"')
		bot.send_message(call.message.chat.id,'Краткое содержание - https://obrazovaka.ru/books/shekspir/gamlet"')
		bot.send_message(call.message.chat.id,'Вернуться',reply_markup=markup_inline)	
	
@bot.message_handler(commands=['gdz'])
def abouts_me(message):
	markup_inline= types.InlineKeyboardMarkup()
	item_1=types.InlineKeyboardButton(text='ДЗ на 11.05',callback_data='a')
	item_2=types.InlineKeyboardButton(text='ДЗ на 12.05',callback_data='b')
	item_3=types.InlineKeyboardButton(text='ДЗ на 13.05',callback_data='c')
	item_4=types.InlineKeyboardButton(text='ДЗ на 14.05',callback_data='d')
	item_5=types.InlineKeyboardButton(text='ДЗ на 17.05',callback_data='e')
	item_6=types.InlineKeyboardButton(text='ДЗ на 18.05',callback_data='f')
	item_7=types.InlineKeyboardButton(text='Что будет 20.05.2021',callback_data='pizda')
	markup_inline.add(item_1,item_2,item_3,item_4,item_5,item_6,item_7)
	bot.send_message(message.chat.id,'Гдз на ближайщие работы',reply_markup=markup_inline)
# @bot.callback_query_handler(func = lambda call: True)
# def dz11(call):

@bot.callback_query_handler(func = lambda call: True)
def answer(call):

	item_back=types.InlineKeyboardButton(text='Вернуться',callback_data='back')
	if call.data=="pizda":
		markup_reply= types.ReplyKeyboardMarkup(resize_keyboard= True)
		item_back=types.KeyboardButton(text='Вернуться')
		markup_reply.add(item_back)
		bot.send_message(call.message.chat.id,'20 числа итоговая контрольная работа по обществознанию, если найду ответы, то они будут здесь, а если нет, то нам пизда',reply_markup=markup_reply)
bot.polling(none_stop=True)
# bot.send_message(message.chat.id,'20 числа итоговая контрольная работа по обществознанию, если найду ответы, то они будут здесь, а если нет, то на пизда',reply_markup=markup_inline)
