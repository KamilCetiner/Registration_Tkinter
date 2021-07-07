
from tkinter import *


def main_screen():
    screen = Tk()
    screen.geometry('300x250')
    screen.title('Notes 1.0')
    Label(text= 'Notes 1.0', bg = 'grey', width= '300', height= '2', font = ('Calibri', 13)).pack()
    Label(text='').pack()
    Button(text = 'Login',  width= '30', height= '2').pack()
    Label(text='').pack()
    Button(text = 'Register',  width= '30', height= '2').pack()
    screen.mainloop()


main_screen()
