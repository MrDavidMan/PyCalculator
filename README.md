# PyCalculator
A Calculator made in Python with Tkinter

## What Is This?
This is a Calculator made in Python 3.6.4 using the module Tkinter for a basic GUI application. This is a basic four function calculator



## Installation 
This program runs on Python 3 and the main driving module for this is Tkinter. 

**WARNING:** This program will **NOT** work if you are running Python 2. The Tkinter module has two variations of itself. One is for Python 2 and the other is for Python 3. This program is written for tkinter version 8.6 and Python 3.6.4.

Tkinter comes packaged with Python 3 so there should be no need to pip install anything.

To test tkinter and check the verison open a command prompt and type:

> `python`

> `import tkinter`

> `tkinter.TkVersion`

This will tell you that tkinter is working and what version is currently installed.

## Using this Program

1) Navigate to the folder that PyCalculator.py is in
2) Launch via clicking the mouse or hitting shift+Right Mouse Button to open a command prompt in the current directory and type `python PyCalculator.py`
3) Once launched the application will open and begin to run until exit

## How this Program runs

The main variable for this program is called root. This assigns the tkinter module to this variable and root is what drives the main GUI application.


### Functions

There are 2 functions outside the class of `root`

The first is called `calcu` this is the main frame of the calculator and will be the holder for all the other elements

The second is called `button` and will allow the buttons to populate

### Class root

The main class of root will create the elements that reside in the frame of calcu

Inside the main class there are three for loops

1) ` for clearButton` This is to create the field where the calculations will displayed and also to clear the field when the corresponding is pressed to wipe the displau

2) `for numButton` This populates the number buttons as well as gives them corrosponding attributes for calculating

4) `for equals` This creates the equals button to finalize calculations\

### Function inside class root

The calc function is the fucntion that pulls the StringVar() and displays in the display field

### Main Loop

`if __name == '__main__':
   root().mainloop()`
   
   
  This will allow us to run our project and supply our code as a library if anyone else wants to use our class and functions



