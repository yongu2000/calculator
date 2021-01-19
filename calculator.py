from tkinter import *
from tkinter import ttk

calculate = ''
temp = 0


def press(button):
    if button == 'AC':
        screen.delete(0, 'end')
        sub_screen.delete(0, 'end')
        print("AC")
    else:
        screen.insert("end", button)
        sub_screen.insert("end", button)
        print(button, "pressed")


def math_press(button):
    global calculate
    global temp
    sub_screen.insert("end", button)
    if not screen.get() == '':
        calculate = button
        temp = int(screen.get())
        screen.delete(0, 'end')
        print(temp, calculate)


def equal_press():
    global calculate
    global temp
    if not (calculate == '' and screen.get() == ''):
        number = int(screen.get())
        if calculate == '/':
            solution = temp / number
        elif calculate == '*':
            solution = temp * number
        elif calculate == '-':
            solution = temp - number
        else:
            solution = temp + number

        screen.delete(0, 'end')
        screen.insert(0, solution)
        print(temp, calculate, number, "=", solution)
        calculate = ''
        temp = 0


calc = Tk()
calc.geometry("350x150")
calc.title("calculator")


enter_val = StringVar(calc, value='')
entered_val = StringVar(calc, value='')

sub_screen = ttk.Entry(calc, textvariable=entered_val, width=20)
sub_screen.grid(row=0, columnspan=3)

screen = ttk.Entry(calc, textvariable=enter_val, width=20)
screen.grid(row=1, columnspan=3)


button7 = ttk.Button(calc, text="7", command=lambda: press('7'))
button7.grid(row=2, column=0)
button8 = ttk.Button(calc, text="8", command=lambda: press('8'))
button8.grid(row=2, column=1)
button9 = ttk.Button(calc, text="9", command=lambda: press('9'))
button9.grid(row=2, column=2)
button_div = ttk.Button(calc, text="/", command=lambda: math_press('/'))
button_div.grid(row=3, column=3)

button4 = ttk.Button(calc, text="4", command=lambda: press('4'))
button4.grid(row=3, column=0)
button5 = ttk.Button(calc, text="5", command=lambda: press('5'))
button5.grid(row=3, column=1)
button6 = ttk.Button(calc, text="6", command=lambda: press('6'))
button6.grid(row=3, column=2)
button_mult = ttk.Button(calc, text="*", command=lambda: math_press('*'))
button_mult.grid(row=2, column=3)

button1 = ttk.Button(calc, text="1", command=lambda: press('1'))
button1.grid(row=4, column=0)
button2 = ttk.Button(calc, text="2", command=lambda: press('2'))
button2.grid(row=4, column=1)
button3 = ttk.Button(calc, text="3", command=lambda: press('3'))
button3.grid(row=4, column=2)
button_add = ttk.Button(calc, text="-", command=lambda: math_press('-'))
button_add.grid(row=4, column=3)

button_ac = ttk.Button(calc, text="AC", command=lambda: press('AC'))
button_ac.grid(row=5, column=0)
button0 = ttk.Button(calc, text="0", command=lambda: press('0'))
button0.grid(row=5, column=1)
button_equal = ttk.Button(calc, text="=", command=lambda: equal_press())
button_equal.grid(row=5, column=2)
button_sub = ttk.Button(calc, text="+", command=lambda: math_press('+'))
button_sub.grid(row=5, column=3)

calc.mainloop()

