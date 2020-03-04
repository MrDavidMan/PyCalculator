import tkinter as tk
from tkinter import *



"""
This is a basic GUI calculator using Python and the module Tkinter for the basic GUI

"""
# Variable for main loop and root
root = tk.Tk()

# Functions

# Creating an intial frame


def calcu(source, side):
    object = Frame(source, borderwidth=4, bd=4, bg="powder blue")
    object.pack(side = side, expand = YES, fill = BOTH)
    return object

# Creating Button

def button(source, side, text, command = None):
    object = Button(source, text=text, command = command)
    object.pack(side = side, expand = YES, fill = BOTH)
    return object




# Classes

class root(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.option_add('*Font', 'arial 20 bold')
        self.pack(expand=YES, fill=BOTH)
        self.master.title('Calculator')
        display = StringVar()

        Entry(self, relief=RIDGE, textvariable=display, justify='right', bd=30, bg="powder blue").pack(side=TOP,expand=YES,fill=BOTH)

        # Below is the function for a "clear button"
        for clearButton in (["C"]):
            erase = calcu(self, TOP)
            for char in clearButton:
                button(erase, LEFT, char, lambda object=display, q=char: object.set(''))

        for numButon in ("789/", "456*", "123-", "0.+"):
            FunctionNum = calcu(self, TOP)
            for equals in numButon:
                button(FunctionNum, LEFT, equals, lambda object = display, q = equals: object.set(object.get() + q))

        EqualButton = calcu(self, TOP)
        for equals in "=":
            if equals == '=':
                btniEquals = button(EqualButton, LEFT, equals)
                btniEquals.bind('<ButtonRelease-1>', lambda e, s=self, object=display: s.calc(object), '+')


            else:
                btniEquals = button(EqualButton, LEFT, equals,
                                    lambda object=display, s=' %s ' % equals: object.set
                                    (object.get() + s))

    def calc(self, display):
        try:
            display.set(eval(display.get()))
        except:
            display.set("ERROR")

# Starting the Program

if __name__== '__main__':
 root().mainloop()