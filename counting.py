import tkinter as tk
from tkinter import Label, Entry, Radiobutton, Button, END
from random import randint

main = tk.Tk()
operation = tk.StringVar()

def get_operation():
    selection = str(operation.get())
    operator.config(text=selection)

Y = "JES"

def generate():
    global Y
    if operation.get() == "+":
        A = randint(1, 99)
        B = randint(1, 100-A)
        Y = A +B

    if operation.get() == "-":
        A = randint(0, 100)
        B = randint(0, A)
        Y = A - B

    if operation.get() == "*":
        A = randint(0, 10)
        B = randint(0, 10)
        Y = A * B

    if operation.get() == "/":
        B = randint(1, 10)
        Y = randint(1, 10)
        A = B*Y

    ent_A.delete(0, END)
    ent_A.insert(0, str(A))
    ent_B.delete(0, END)
    ent_B.insert(0,str(B))

def check():
    if Y == int(ent_result.get()):
        lbl_correct.config(text="Spravně")
    else:
        lbl_correct.config(text="Špatně")


lbl_operace = Label(main, text=u"Operace: ").grid(row=0, column=0, columnspan=1)

radio_plus = Radiobutton(main, text="+", value="+", variable=operation, command=get_operation)
radio_plus.grid(row=0, column=1)

radio_minus = Radiobutton(main, text="-", value="-", variable=operation, command=get_operation)
radio_minus.grid(row=0, column=2)

radio_times = Radiobutton(main, text="*", value="*", variable=operation, command=get_operation)
radio_times.grid(row=0, column=3)

radio_divide = Radiobutton(main, text="/", value="/", variable=operation, command=get_operation)
radio_divide.grid(row=0, column=4)

ent_A= Entry(main, width=5)
ent_A.grid(row=1, column=0)

operator= Label(main, text="Vyber znamenko")
operator.grid(row=1, column=1)

ent_B= Entry(main, width=5)
ent_B.grid(row=1, column=2)

lbl_equals = Label(main, text="=", width=5)
lbl_equals.grid(row=1, column=3)

ent_result = Entry(main, width=5)
ent_result.grid(row=1, column=4)

but_new=Button(main, text="Nový příklad", command=generate)
but_new.grid(row=2, column=0)

but_new=Button(main, text="Kontrola", command=check)
but_new.grid(row=2, column=1)

lbl_correct = Label(main, text="")
lbl_correct.grid(row=2, column=2)

main.mainloop()
