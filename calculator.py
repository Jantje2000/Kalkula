from tkinter import *
import re

gui = Tk()
gui.title("Calculator")
gui.geometry("500x500")

def solve():
    solve = eval(calc.get())
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
plus = Button(gui, text="+", width=8, height=4, command=lambda: number("+"))
plus.place(relx=.81, rely=.2, anchor="c")

#row 2
one = Button(gui, text="1", width=8, height=4, command=lambda: number(1))
one.place(relx=.15, rely=.35, anchor="c")
two = Button(gui, text="2", width=8, height=4, command=lambda: number(2))
two.place(relx=.37, rely=.35, anchor="c")
three = Button(gui, text="3", width=8, height=4, command=lambda: number(3))
three.place(relx=.59, rely=.35, anchor="c")
minus = Button(gui, text="-", width=8, height=4, command=lambda: number("-"))
minus.place(relx=.81, rely=.35, anchor="c")

#row 3
four = Button(gui, text="4", width=8, height=4, command=lambda: number(4))
four.place(relx=.15, rely=.5, anchor="c")
five = Button(gui, text="5", width=8, height=4, command=lambda: number(5))
five.place(relx=.37, rely=.5, anchor="c")
six = Button(gui, text="6", width=8, height=4, command=lambda: number(6))
six.place(relx=.59, rely=.5, anchor="c")
time = Button(gui, text="*", width=8, height=4, command=lambda: number("*"))
time.place(relx=.81, rely=.5, anchor="c")

#row 4
seven = Button(gui, text="7", width=8, height=4, command=lambda: number(7))
seven.place(relx=.15, rely=.65, anchor="c")
eight = Button(gui, text="8", width=8, height=4, command=lambda: number(8))
eight.place(relx=.37, rely=.65, anchor="c")
nine = Button(gui, text="9", width=8, height=4, command=lambda: number(9))
nine.place(relx=.59, rely=.65, anchor="c")
part = Button(gui, text="/", width=8, height=4, command=lambda: number("/"))
part.place(relx=.81, rely=.65, anchor="c")

#row 5
negative = Button(gui, text="-", width=8, height=4, command=lambda: number("--"))
negative.place(relx=.15, rely=.80, anchor="c")
zero = Button(gui, text="0", width=8, height=4, command=lambda: number(0))
zero.place(relx=.37, rely=.80, anchor="c")
comma = Button(gui, text=",", width=8, height=4, command=lambda: number(","))
comma.place(relx=.59, rely=.80, anchor="c")
part = Button(gui, text="=", width=8, height=4, command=solve)
part.place(relx=.81, rely=.80, anchor="c")

gui.mainloop()
