#Text
#

from tkinter import *

root = Tk()
root.title("Text")

texto = Text(root)
texto.pack()
texto.config(width=40, height=15, padx=15, pady=15, font=("Curier, 11"),selectbackground="blue")

label = Label(root, text="Escribe aqui")
label.pack()
label.config(bg="green", font="Curier, 20")




root.mainloop()