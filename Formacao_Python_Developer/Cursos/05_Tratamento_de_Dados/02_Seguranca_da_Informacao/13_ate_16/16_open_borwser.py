import webbrowser
from tkinter import *

root = Tk( )

root.title('Abrir Borwser')
root.geometry('300x200')

def google():
    webbrowser.open('www.google.com')

mygoogle = Button(root, text='Abrir o Google', command=google).pack(pady=20)

root.mainloop()