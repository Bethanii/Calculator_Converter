import tkinter
from tkinter import *
from tkinter import messagebox, StringVar
expression = ""


def calc_window():
    input_text = StringVar()

    win = Toplevel(gui)
    win.geometry("312x324")
    win.resizable(0, 0)
    win.title("Calculator")

    def btn_click(i):
        global expression
        expression = expression + str(i)
        input_text.set(expression)

    def bt_clear():
        global expression
        expression = ""
        input_text.set("")

    def bt_equal():
        global expression
        result = str(eval(expression))
        input_text.set(result)
        expression = ""

    input_frame = Frame(win, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black",
                        highlightthickness=2)

    input_frame.pack(side=TOP)

    input_field = Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg="#eee", bd=0,
                        justify=RIGHT)

    input_field.grid(row=0, column=0)

    input_field.pack(ipady=10)

    btns_frame = Frame(win, width=312, height=272.5, bg="grey")

    btns_frame.pack()

    # first row

    clear = Button(btns_frame,text="C", fg="black", width=32, height=3, bd=0, bg="#eee", cursor="hand2",
                   command=lambda: bt_clear()).grid(row=0, column=0, columnspan=3, padx=1, pady=1)

    divide = Button(btns_frame, text="/", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
                    command=lambda: btn_click("/")).grid(row=0, column=3, padx=1, pady=1)

    # second row

    seven = Button(btns_frame, text="7", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                   command=lambda: btn_click(7)).grid(row=1, column=0, padx=1, pady=1)

    eight = Button(btns_frame, text="8", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                   command=lambda: btn_click(8)).grid(row=1, column=1, padx=1, pady=1)

    nine = Button(btns_frame, text="9", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                  command=lambda: btn_click(9)).grid(row=1, column=2, padx=1, pady=1)

    multiply = Button(btns_frame, text="*", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
                      command=lambda: btn_click("*")).grid(row=1, column=3, padx=1, pady=1)

    # third row

    four = Button(btns_frame, text="4", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                  command=lambda: btn_click(4)).grid(row=2, column=0, padx=1, pady=1)

    five = Button(btns_frame, text="5", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                  command=lambda: btn_click(5)).grid(row=2, column=1, padx=1, pady=1)

    six = Button(btns_frame, text="6", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                 command=lambda: btn_click(6)).grid(row=2, column=2, padx=1, pady=1)

    minus = Button(btns_frame, text="-", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
                   command=lambda: btn_click("-")).grid(row=2, column=3, padx=1, pady=1)

    # fourth row

    one = Button(btns_frame, text="1", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                 command=lambda: btn_click(1)).grid(row=3, column=0, padx=1, pady=1)

    two = Button(btns_frame, text="2", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                 command=lambda: btn_click(2)).grid(row=3, column=1, padx=1, pady=1)

    three = Button(btns_frame, text="3", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                   command=lambda: btn_click(3)).grid(row=3, column=2, padx=1, pady=1)

    plus = Button(btns_frame, text="+", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
                  command=lambda: btn_click("+")).grid(row=3, column=3, padx=1, pady=1)

    # fourth row

    zero = Button(btns_frame, text="0", fg="black", width=21, height=3, bd=0, bg="#fff", cursor="hand2",
                  command=lambda: btn_click(0)).grid(row=4, column=0, columnspan=2, padx=1, pady=1)

    point = Button(btns_frame, text=".", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
                   command=lambda: btn_click(".")).grid(row=4, column=2, padx=1, pady=1)

    equals = Button(btns_frame, text="=", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
                    command=lambda: bt_equal()).grid(row=4, column=3, padx=1, pady=1)


gui = Tk()
gui.geometry("512x524")
gui.resizable(0, 0)
gui.configure(background="pink")
gui.title("Calculator/Converter")

var = StringVar()
blank_label = Label(gui,
                    textvariable=var,
                    text="k",
                    bg="RosyBrown1",
                    width=20,
                    height=7,
                    anchor=CENTER,
                    padx=4)
blank_label.pack(fill="both")

start_label = Label(gui,
                    text="Chose the function you would like to use",
                    bg="pink",
                    width=20,
                    height=7,
                    anchor=CENTER,
                    padx=4)

start_label.pack(fill="both")

b1 = Button(gui,
            text="Calculator",
            width=18,
            height=5,
            bg="mediumpurple1",
            command=calc_window)

b1.pack(side=LEFT, fill="none", expand=True)

b2 = Button(gui,
            text="Converter",
            width=18,
            height=5,
            bg="mediumpurple1")
b2.pack(side=RIGHT, fill="none", expand=True)
gui.mainloop()


def number_systems():
    choice = "1. Decimal \n2. Binary"
    return choice


def decimal_to_binary(i):
    i = bin(i)
    if i.startswith('0b'):
        return i[len('0b'):]
    return i


def binary_to_decimal(i):
    d = int(i, 2)
    return str(d)

system1 = int(input("Choose the number system you want to convert from: \n" + number_systems()) + "\n")
system2 = int(input("Choose the number system you want to convert to: \n" + number_systems()) + "\n")

if system1 == 1:
    num1 = int(input("Enter the decimal number: "))
    print((str(num1) + " in binary is: " + decimal_to_binary(num1)))
elif system1 == 2:
    num1 = str(input("Enter the binary number: "))
    print((num1 + " in decimal is: " + binary_to_decimal(num1)))
