import tkinter
from tkinter import *
from tkinter import messagebox, StringVar
from tkinter import ttk
import tkinter as tk
import CalculatorWindow
expression = ""
gui = Tk()

def convert_window():
    win = Toplevel(gui)
    win.geometry("350x250")
    win.resizable(0, 0)
    win.title("Converter")

# Label
    ttk.Label(win, text = "Select the system :",
              font=("Times New Roman", 10)).grid(column=0, row=15, padx=10, pady=25)

    v = tk.StringVar()
    system_chosen = ttk.Combobox(win, width=27,
                                 textvariable=v)

    system_chosen['values'] = ('Decimal',
                               'Binary')

    system_chosen.grid(column=1, row=15)

    system_chosen.current(1)
    win.mainloop()


# Main loop starts
def MainLoop():

    gui.geometry("450x475")
    gui.resizable(0, 0)
    gui.configure(background="white smoke")
    gui.title("Calculator/Converter")

    var = StringVar()
    blank_label = Label(gui,
                        textvariable=var,
                        text="k",
                        bg="white smoke",
                        width=20,
                        height=7,
                        anchor=CENTER,
                        padx=4)
    blank_label.pack(fill="both")

    start_label = Label(gui,
                        text="Chose the function you would like to use",
                        bg="white smoke",
                        width=40,
                        height=7,
                        anchor=CENTER,)

    start_label.pack(fill="both")

    b1 = Button(text="Calculator",
                width=18,
                height=5,
                bg="Light blue",
                command=CalculatorWindow.calc_window)

    b1.pack(side=LEFT, fill="none", expand=True)

    b2 = Button(gui,
                text="Converter",
                width=18,
                height=5,
                bg="Light blue",
                command=convert_window)

    b2.pack(side=RIGHT, fill="none", expand=True)
    gui.mainloop()
