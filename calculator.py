from tkinter import *   #this is the gui library
from math import *      #we need this for handling the root square
import re

gui = Tk()
gui.title("Calculator")
gui.geometry("500x500")

def clear_one():
    calc_split = re.split('[+ - * / ^ V(]', calc.get())
    calc.delete(len(calc.get())-len(calc_split[len(calc_split) - 1]), END)

def clear():
    calc.delete(0, END)

def backspace():
    calc_length = len(calc.get()) - 1
    calc.delete(calc_length, END)

def solve():
    if re.search('[a-zA-Z]', calc.get()):
        calc.delete(0, END)
    else:
        my_calc = calc.get()
        my_calc = my_calc.replace("V", "sqrt")
        my_calc = my_calc.replace("^", "**")

        if "(" in my_calc:
            parentheses_in_my_calc = my_calc.count("(")
            print(parentheses_in_my_calc)
            for parenthese in range(0, parentheses_in_my_calc):
                last_char = my_calc.split("(", 1)[0][1::]
                if last_char != "*" and last_char != "/" and last_char != "+" and last_char != "-" and last_char != "sqrt" and last_char != "**":
                    length = len(last_char)
                    print("de lengte is dus")
                    my_calc = my_calc[:length + 1:] + "*(" + my_calc[len(my_calc) - len(my_calc[length]) - 1::]

        print(my_calc)
        solve = eval(my_calc)

        calc.delete(0, END)
        calc.insert(0, solve)

def number(digit):
    length = len(calc.get())
    if digit != "--":
        calc.insert(length, digit)
    else:
        if calc.get()[:1:] == "-":
            my_calc = calc.get()[1::]
            calc.delete(0, END)
            calc.insert(0, my_calc)
        else:
            my_calc = calc.get()
            calc.delete(0, END)
            calc.insert(length, digit[1::] + my_calc)


calc = Entry(gui, width=40)
calc.place(relx=.5, rely=.1, anchor="c")
calc.focus_set()

#row 1
parenthese1 = Button(gui, text="(", width=8, height=4, command=lambda: number("("))
parenthese1.place(relx=.15, rely=.20, anchor="c")
parenthese2 = Button(gui, text=")", width=8, height=4, command=lambda: number(")"))
parenthese2.place(relx=.37, rely=.20, anchor="c")
square_root = Button(gui, text="V", width=8, height=4, command=lambda: number("V("))
square_root.place(relx=.59, rely=.20, anchor="c")
square = Button(gui, text="^", width=8, height=4, command=lambda: number("^"))
square.place(relx=.81, rely=.20, anchor="c")

#row 2
clear = Button(gui, text="Clear", width=8, height=4, command=clear)
clear.place(relx=.15, rely=.35, anchor="c")
clear_once = Button(gui, text="CE", width=8, height=4, command=clear_one)
clear_once.place(relx=.37, rely=.35, anchor="c")
backspace = Button(gui, text="X<", width=8, height=4, command=backspace)
backspace.place(relx=.59, rely=.35, anchor="c")
plus = Button(gui, text="+", width=8, height=4, command=lambda: number("+"))
plus.place(relx=.81, rely=.35, anchor="c")

#row 3
one = Button(gui, text="1", width=8, height=4, command=lambda: number(1))
one.place(relx=.15, rely=.5, anchor="c")
two = Button(gui, text="2", width=8, height=4, command=lambda: number(2))
two.place(relx=.37, rely=.5, anchor="c")
three = Button(gui, text="3", width=8, height=4, command=lambda: number(3))
three.place(relx=.59, rely=.5, anchor="c")
minus = Button(gui, text="-", width=8, height=4, command=lambda: number("-"))
minus.place(relx=.81, rely=.5, anchor="c")

#row 4
four = Button(gui, text="4", width=8, height=4, command=lambda: number(4))
four.place(relx=.15, rely=.65, anchor="c")
five = Button(gui, text="5", width=8, height=4, command=lambda: number(5))
five.place(relx=.37, rely=.65, anchor="c")
six = Button(gui, text="6", width=8, height=4, command=lambda: number(6))
six.place(relx=.59, rely=.65, anchor="c")
time = Button(gui, text="*", width=8, height=4, command=lambda: number("*"))
time.place(relx=.81, rely=.65, anchor="c")

#row 5
seven = Button(gui, text="7", width=8, height=4, command=lambda: number(7))
seven.place(relx=.15, rely=.80, anchor="c")
eight = Button(gui, text="8", width=8, height=4, command=lambda: number(8))
eight.place(relx=.37, rely=.80, anchor="c")
nine = Button(gui, text="9", width=8, height=4, command=lambda: number(9))
nine.place(relx=.59, rely=.80, anchor="c")
part = Button(gui, text="/", width=8, height=4, command=lambda: number("/"))
part.place(relx=.81, rely=.80, anchor="c")

#row 6
negative = Button(gui, text="-", width=8, height=4, command=lambda: number("--"))
negative.place(relx=.15, rely=.95, anchor="c")
zero = Button(gui, text="0", width=8, height=4, command=lambda: number(0))
zero.place(relx=.37, rely=.95, anchor="c")
comma = Button(gui, text=",", width=8, height=4, command=lambda: number(","))
comma.place(relx=.59, rely=.95, anchor="c")
part = Button(gui, text="=", width=8, height=4, command=solve)
part.place(relx=.81, rely=.95, anchor="c")

gui.mainloop()
