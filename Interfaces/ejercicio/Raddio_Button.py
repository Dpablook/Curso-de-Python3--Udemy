from tkinter import *

def mostrar():
	if opciones.get()==1:
		label2.config(text="Haz elegido Masculino")
	elif opciones.get()==2:
		label2.config(text="Haz elegido Femenino")
	else:
		label2.config(text="Haz elegido Otro")

root=Tk()

opciones = IntVar()

label1 = Label(root, text="Elige un genero")
label1.pack()

Radiobutton(root, text="Masculino", variable=opciones, value=1, command=mostrar).pack()
Radiobutton(root, text="Femenino", variable=opciones, value=2, command=mostrar).pack()
Radiobutton(root, text="Otro", variable=opciones, value=3, command=mostrar).pack()

label2 = Label(root)
label2.pack()

root.mainloop()