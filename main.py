import tkinter
from tkinter import *

gui = Tk()
gui.geometry("512x524")
gui.resizable(0, 0)
gui.title("Calculator/Converter")

var=StringVar()
start_label = Label(gui,
                    textvariable=var,
                    bg="white",
                    relief="raised",
                    width=15,
                    height=7,
                    anchor=CENTER,
                    padx=4)
var.set("label")
start_label.pack()

start_label.pack()
b1 = Button(gui,
            text="Button one",
            width=10,
            height=5)
b1.pack(anchor=CENTER)

b2 = Button(gui,
            text="Button two",
            width=10,
            height=5)
b2.pack(anchor=CENTER)


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
