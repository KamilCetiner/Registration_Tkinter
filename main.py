
from tkinter import *

def register():
    screen1 = Toplevel(screen)
    screen1.title('Register')
    screen1.geometry('300x250')
    
    username = StringVar()
    password = StringVar()

    Label(screen1, text='Please enter details below').pack()
    Label(screen1, text='').pack()
    Label(screen1, text='Username *').pack()
    Entry(screen1, textvariable = username).pack()
    Label(screen1,text='Password *').pack()
    Entry(screen1,textvariable= password).pack()
    Label(screen1, text='').pack()
    Label(screen1, text='').pack()
    Label(screen1, text='').pack()
    Label(screen1, text='').pack()
    Label(screen1, text='').pack()
    Label(screen1, text='').pack()
    Label(screen1, text='').pack()
    Button(screen1, text= 'Register', width = 10, height = 1).pack()


def login():
    print('Login started')






def main_screen():
    global screen
    screen = Tk()
    screen.geometry('300x250')
    screen.title('Notes 1.0')
    Label(text= 'Notes 1.0', bg = 'grey', width= '300', height= '2', font = ('Calibri', 13)).pack()
    Label(text='').pack()
    Button(text = 'Login',  width= '30', height= '2', command = login).pack()
    Label(text='').pack()
    Button(text = 'Register',  width= '30', height= '2', command = register).pack()
    screen.mainloop()


main_screen()
