# coding: utf-8

from tkinter.messagebox import *
from tkinter import *


def callback():
    if askyesno('ATTENTION', 'BRAVOO'):
        showwarning('FAIT PAS CA', 'VOUS AVEZ PERDU...')
    else:
        showinfo('DERNIERE CHANCE', 'Etes vous vraiment sûr?')
        showerror("MAUVAIS CHOIX", "Aha")



fenetre = Tk()

label = Label(fenetre, text="Bonjours les jeunes")
label.pack()
Button(text='NE PAS CLIQUE', command=callback).pack()

fenetre.mainloop()


