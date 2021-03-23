from tkinter import *
from datetime import datetime
def equal_calc():
	a = calc_entry.get()
	b = eval(a)
	calc_entry.delete(0, END)
	calc_entry.insert(END, str(b))

def programs():
	if like.get() == 2:
		Radiobutton_1.place_forget()
		Radiobutton_2.place_forget()
		Radiobutton_3.place_forget()
		vib_programs.place_forget()
		start_b_1.place_forget()
		start_b_2.place_forget()
		l_start.place_forget()
		calc_button_1 = Button(width = 6, height = 2, bg = '#808080', bd = 3, text = '7', font = ('Comic Sans MS', 20), activeforeground = 'white', activebackground = '#4d4d4d', command = lambda text = '7': calc_entry.insert(END, text)) 
		calc_button_1.place(x = 70, y = 100)
		calc_button_2 = Button(width = 6, height = 2, bg = '#808080', bd = 3, text = '4', font = ('Comic Sans MS', 20), activeforeground = 'white', activebackground = '#4d4d4d', command = lambda text = '4': calc_entry.insert(END, text))
		calc_button_2.place(x = 70, y = 215)
		calc_button_3 = Button(width = 6, height = 2, bg = '#808080', bd = 3, text = '1', font = ('Comic Sans MS', 20), activeforeground = 'white', activebackground = '#4d4d4d', command = lambda text = '1': calc_entry.insert(END, text))
		calc_button_3.place(x = 70, y = 330)
		calc_button_4 = Button(width = 6, height = 2, bg = '#808080', bd = 3, text = '8', font = ('Comic Sans MS', 20), activeforeground = 'white', activebackground = '#4d4d4d', command = lambda text = '8': calc_entry.insert(END, text))
		calc_button_4.place(x = 185, y = 100)
		calc_button_5 = Button(width = 6, height = 2, bg = '#808080', bd = 3, text = '5', font = ('Comic Sans MS', 20), activeforeground = 'white', activebackground = '#4d4d4d', command = lambda text = '5': calc_entry.insert(END, text))
		calc_button_5.place(x = 185, y = 215)
		calc_button_6 = Button(width = 6, height = 2, bg = '#808080', bd = 3, text = '2', font = ('Comic Sans MS', 20), activeforeground = 'white', activebackground = '#4d4d4d', command = lambda text = '2': calc_entry.insert(END, text))
		calc_button_6.place(x = 185, y = 330)
		calc_button_7 = Button(width = 6, height = 2, bg = '#808080', bd = 3, text = '9', font = ('Comic Sans MS', 20), activeforeground = 'white', activebackground = '#4d4d4d', command = lambda text = '9': calc_entry.insert(END, text))
		calc_button_7.place(x = 300, y = 100)
		calc_button_8 = Button(width = 6, height = 2, bg = '#808080', bd = 3, text = '6', font = ('Comic Sans MS', 20), activeforeground = 'white', activebackground = '#4d4d4d', command = lambda text = '6': calc_entry.insert(END, text))
		calc_button_8.place(x = 300, y = 215)
		calc_button_9 = Button(width = 6, height = 2, bg = '#808080', bd = 3, text = '3', font = ('Comic Sans MS', 20), activeforeground = 'white', activebackground = '#4d4d4d', command = lambda text = '3': calc_entry.insert(END, text))
		calc_button_9.place(x = 300, y = 330)
		calc_button_10 = Button(width = 6, height = 2, bg = '#808080', bd = 3, text = '0', font = ('Comic Sans MS', 20), activeforeground = 'white', activebackground = '#4d4d4d', command = lambda text = '0': calc_entry.insert(END, text))
		calc_button_10.place(x = 185, y = 445)
		calc_button_plus = Button(width = 4, height = 1, bg = '#808080', bd = 3, text = '+', font = ('Comic Sans MS', 20), activeforeground = 'white', activebackground = '#4d4d4d', command = lambda text = '+': calc_entry.insert(END, text))
		calc_button_plus.place(x = 415, y = 100)
		calc_button_minus = Button(width = 4, height = 1, bg= '#808080', bd = 3, text = '-', font = ('Comic Sans MS', 20), activeforeground = 'white', activebackground = '#4d4d4d', command = lambda text = '-': calc_entry.insert(END, text))
		calc_button_minus.place(x = 500, y = 100)
		calc_button_multiply = Button(width = 4, height = 1, bg= '#808080', bd = 3, text = '*', font = ('Comic Sans MS', 20), activeforeground = 'white', activebackground = '#4d4d4d', command = lambda text = '*': calc_entry.insert(END, text))
		calc_button_multiply.place(x = 415, y = 185)
		calc_button_split = Button(width = 4, height = 1, bg= '#808080', bd = 3, text = '/', font = ('Comic Sans MS', 20), activeforeground = 'white', activebackground = '#4d4d4d', command = lambda text = '/': calc_entry.insert(END, text))
		calc_button_split.place(x = 500, y = 185)
		calc_button_grade = Button(width = 4, height = 1, bg= '#808080', bd = 3, text = '**', font = ('Comic Sans MS', 20), activeforeground = 'white', activebackground = '#4d4d4d', command = lambda text = '**': calc_entry.insert(END, text))
		calc_button_grade.place(x = 415, y = 270)
		calc_button_equal = Button(width = 4, height = 1, bg= '#808080', bd = 3, text = '=', font = ('Comic Sans MS', 20), activeforeground = 'white', activebackground = '#4d4d4d', command = equal_calc)
		calc_button_equal.place(x = 457, y = 355)
		global calc_entry
		calc_entry = Entry(width = 21, bd = 4, text = ' ', font = ('Comic Sans MS', 20))
		calc_entry.place(x = 70, y = 50)

def start_b_1_games():
	l_start['text'] = 'games'
def start_b_2_programs(): #Функция, отвечающая за нажатие кнопки 'Программы'
	global like
	like = IntVar()
	like.set(None)
	global Radiobutton_1
	Radiobutton_1 = Radiobutton(root, text = 'Таймер', font = ('Comic Sans MS', 15), variable = like, value = 1)
	Radiobutton_1.place(x = 400, y = 210)
	global Radiobutton_2
	Radiobutton_2 = Radiobutton(root, text = 'Калькулятор', font = ('Comic Sans MS', 15), variable = like, value = 2)
	Radiobutton_2.place(x = 400, y = 260)
	global Radiobutton_3
	Radiobutton_3 = Radiobutton(root, text = 'Что-то еще...', font = ('Comic Sans MS', 15), variable = like, value = 3)
	Radiobutton_3.place(x = 400, y = 310)
	global vib_programs
	vib_programs = Button(width = 10, height = 1, bg = '#808080', text = 'Выбрать', font = ('Comic Sans MS', 12), activeforeground = 'white', activebackground = '#4d4d4d', command = programs)
	vib_programs.place(x = 420, y = 370)
root = Tk()
root.title('BETA')
root.geometry('600x600')

l_start = Label(text = 'Здравствуйте! Чем хотите заняться?', font = ('Comic Sans MS', 15))
l_start.place(x = 130, y = 100)
start_b_1 = Button(width = 10, height = 1, text = 'Игры', font = ('Comic Sans MS', 15), bg = '#808080', activeforeground = 'white', activebackground = '#4d4d4d', command = start_b_1_games) #Кнопка для вывода игр
start_b_2 = Button(width = 10, height = 1, text = 'Программы', font = ('Comic Sans MS', 15), bg = '#808080', activeforeground = 'white', activebackground = '#4d4d4d', command = start_b_2_programs) # Кнопка для вывода программ
start_b_1.place(x = 90, y = 150)
start_b_2.place(x = 400, y = 150)


root.mainloop()