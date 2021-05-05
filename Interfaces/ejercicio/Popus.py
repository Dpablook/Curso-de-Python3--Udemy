#Los popus o ventanas emergentes
#


from tkinter import *
from tkinter import messagebox #a los popus hay que importalos aparte

def salir():
	i = messagebox.askquestion("Salir", "Estas seguro que deseas salir?")
	if i == "yes":
		root.destroy()

def acerca():
	messagebox.showinfo("Informacion", "Creado por Pablo")



root=Tk()
root.title("Menu")

barraMenu = Menu(root)
root.config(menu=barraMenu)

archivoMenu=Menu(barraMenu, tearoff=0)#Con esto se elimina la barrita de abajo
barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
archivoMenu.add_command(label="Nueva Archivo")
archivoMenu.add_command(label="Nueva Ventana", command=acerca)
archivoMenu.add_command(label="Salir", command=salir)

archivoEditar=Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Editar", menu=archivoEditar)
archivoEditar.add_command(label="Deshacer")
archivoEditar.add_command(label="Rehacer")


root.mainloop()