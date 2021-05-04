from tkinter import *

root = Tk()
root.geometry("400x400")

productos = Label(root, text="Producto")
productos.pack()

def Agregar():
	listaProductos.insert(END, entrada.get())
def Eliminar():
	listaProductos.delete(END, entrada.get())


listaProductos = Listbox(root, width=50)
listaProductos.insert(0, "Carne")
listaProductos.insert(1, "Pollo")
listaProductos.insert(2, "Pescado")
listaProductos.insert(3, "Verdura")
listaProductos.insert(4, "Fruta")
listaProductos.pack()

#Eliminar productos:
#
# listaProductos.delete(0)#Se elimina carne

entrada = Entry(root)
entrada.pack()

boton1= Button(root, text="Agregar", command=Agregar)
boton1.pack()

#no funciono :(
boton2= Button(root, text="Eliminar", command=Eliminar)
boton2.pack()


root.mainloop()