import tkinter as tk
from tkinter import Label, Button, Frame, Entry
from functools import partial
from random import randint, choice

class Problem():
    def __init__(self):
        self.select_operation()
        self.generate()

    def insert_values(self):
        lbl_a.config(text=self.a)
        lbl_operation.config(text=self.operation)
        lbl_b.config(text=self.b)

    def select_operation(self):
        choose = ent_operators.get()
        if choose:
            self.operation = choice(choose)
        else:
            self.operation = choice("+-*/")

    def generate(self):
        if self.operation == "+":
            a = randint(1, 99)
            b = randint(1, 100-a)
            y = a +b

        if self.operation == "-":
            a = randint(0, 100)
            b = randint(0, a)
            y = a - b

        if self.operation == "*":
            a = randint(0, 10)
            b = randint(0, 10)
            y = a * b

        if self.operation == "/":
            b = randint(1, 10)
            y = randint(1, 10)
            a = b * y
        #nechtělo se mi ke všem připisovat self :P
        self.a = a
        self.b = b
        self.y = y

    def check(self):
        answer = ent_answer.get()
        if self.y == int(answer):
            lbl_correct.config(text="Správně", bg="lightgreen")
        else:
            lbl_correct.config(text="Špatně", bg="pink")

def new():
    #jojo prasárna
    global problem
    lbl_correct.config(text="čekám", bg="white")
    problem = Problem()
    problem.insert_values()

def check():
    global problem
    problem.check()

main = tk.Tk()

fr_operators = Frame(main)
fr_operators.grid(row=0, column=0)

lbl_operators = Label(fr_operators, text="Vypište znaménka:")
lbl_operators.grid(row=0, column=0)

ent_operators = Entry(fr_operators)
ent_operators.grid(row=0, column=1)

#prasárna numero dos
problem = Problem()

fr_buttons = Frame(main)
fr_buttons.grid(row=1, column=0)

bt_new = Button(fr_buttons, text="Nový příklad", command=new)
bt_new.grid(row=0, column=0)

bt_new = Button(fr_buttons, text="Kontrola", command=check)
bt_new.grid(row=0, column=1)

lbl_correct = Label(fr_buttons, text="čekám")
lbl_correct.grid(row=0, column=2)

fr_problem = Frame(main)
fr_problem.grid(row=2, column=0)

lbl_a = Label(fr_problem)
lbl_a.grid(row=0, column=0)

lbl_operation = Label(fr_problem)
lbl_operation.grid(row=0, column=1)

lbl_b = Label(fr_problem)
lbl_b.grid(row=0, column=2)

lbl_equals = Label(fr_problem, text="=")
lbl_equals.grid(row=0, column=3)

ent_answer = Entry(fr_problem)
ent_answer.grid(row=0, column=4)

problem.insert_values()

main.mainloop()
