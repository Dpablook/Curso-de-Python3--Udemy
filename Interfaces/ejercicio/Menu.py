from tkinter import *

root=Tk()
root.title("Menu")

barraMenu = Menu(root)
root.config(menu=barraMenu)

archivoMenu=Menu(barraMenu, tearoff=0)#Con esto se elimina la barrita de abajo
barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
archivoMenu.add_command(label="Nueva Archivo")
archivoMenu.add_command(label="Nueva Ventana")
archivoMenu.add_command(label="Salir")

archivoEditar=Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Editar", menu=archivoEditar)
archivoEditar.add_command(label="Deshacer")
archivoEditar.add_command(label="Rehacer")


root.mainloop()