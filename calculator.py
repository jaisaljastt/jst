from tkinter import *


def button_press(num):
    global equation_text
    equation_text = equation_text + str(num)
    equation_label.set(equation_text)


def clear():
    global equation_text
    equation_text = ""
    equation_label.set(equation_text)


def equal():
    try:
        global equation_text
        total = str(eval(equation_text))
        equation_label.set(total)
        equation_text = total
    except ZeroDivisionError:
        equation_label.set("Zero Division, Fool")
    except SyntaxError:
        equation_label.set("Syntax Error, Fool")


window = Tk()

window.title("Calculator")
window.geometry("340x340")
window.resizable(0, 0)

menu_bar = Menu(window)  # menu
window.config(menu=menu_bar)

about_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='About', menu=about_menu)
about_menu.add_command(label='jST™', font=('Arial', 10))

equation_text = ""
equation_label = StringVar()
screen = Label(window, textvariable=equation_label, bg='#eded95', font=('fixedsys', 20), height=2, width=24)
screen.pack()

frame = Frame(window)
frame.pack()

button1 = Button(frame, text='1', bg='black', fg='yellow', height=3, width=10, relief="groove", command=lambda: button_press(1))
button1.grid(row=0, column=0)
button2 = Button(frame, text='2', bg='black', fg='yellow', height=3, width=10, relief="groove", command=lambda: button_press(2))
button2.grid(row=0, column=1)
button3 = Button(frame, text='3', bg='black', fg='yellow', height=3, width=10, relief="groove", command=lambda: button_press(3))
button3.grid(row=0, column=2)
button4 = Button(frame, text='4', bg='black', fg='yellow', height=3, width=10, relief="groove", command=lambda: button_press(4))
button4.grid(row=1, column=0)
button5 = Button(frame, text='5', bg='black', fg='yellow', height=3, width=10, relief="groove", command=lambda: button_press(5))
button5.grid(row=1, column=1)
button6 = Button(frame, text='6', bg='black', fg='yellow', height=3, width=10, relief="groove", command=lambda: button_press(6))
button6.grid(row=1, column=2)
button7 = Button(frame, text='7', bg='black', fg='yellow', height=3, width=10, relief="groove", command=lambda: button_press(7))
button7.grid(row=2, column=0)
button8 = Button(frame, text='8', bg='black', fg='yellow', height=3, width=10, relief="groove", command=lambda: button_press(8))
button8.grid(row=2, column=1)
button9 = Button(frame, text='9', bg='black', fg='yellow', height=3, width=10, relief="groove", command=lambda: button_press(9))
button9.grid(row=2, column=2)
button0 = Button(frame, text='0', bg='black', fg='yellow', height=3, width=10, relief="groove", command=lambda: button_press(0))
button0.grid(row=3, column=1)
add_button = Button(frame, text='+', bg='black', fg='yellow', height=3, width=10, relief="groove", command=lambda: button_press('+'))
add_button.grid(row=3, column=0)
sub_button = Button(frame, text='--', bg='black', fg='yellow', height=3, width=10, relief="groove", command=lambda: button_press('-'))
sub_button.grid(row=3, column=2)
clear_button = Button(frame, text='C', bg='#ffff03', height=3, width=13, relief="groove", command=clear)
clear_button.grid(row=0, column=4)
mul_button = Button(frame, text='*', bg='#b3b320', height=3, width=13, relief="groove", command=lambda: button_press('*'))
mul_button.grid(row=2, column=4)
div_button = Button(frame, text='/', bg='#cfcf1b', height=3, width=13, relief="groove", command=lambda: button_press('/'))
div_button.grid(row=1, column=4)
decimal = Button(frame, text='.', bg='#8a8a24', height=3, width=13, relief="groove", command=lambda: button_press('.'))
decimal.grid(row=3, column=4)
equal_button = Button(window, text='=', bg='#707022', height=3, relief="groove", width=48, command=equal)
equal_button.pack()

window.mainloop()
