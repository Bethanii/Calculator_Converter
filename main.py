import tkinter
from tkinter import *
from tkinter import messagebox


def calc_window():
    newwindow = Toplevel(gui)
    newwindow.geometry("512x524")
    newwindow.resizable(0, 0)
    newwindow.title("new window")

    one = Button(gui,
                 text="1",
                 width=18,
                 height=5,
                 bg="mediumpurple1")
    one.grid(row="1", column="2")

    one = Button(gui,
                 text="1",
                 width=18,
                 height=5,
                 bg="mediumpurple1")
    one.grid(row="1", column="2")


gui = Tk()
gui.geometry("512x524")
gui.resizable(0, 0)
gui.configure(background="pink")
gui.title("Calculator/Converter")

var=StringVar()
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
