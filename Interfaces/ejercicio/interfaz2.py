from tkinter import *

#Crear una ventana
#root.titulo para nombrarla

root=Tk()#creamos la ventana


#aca va todo el contenido de la ventana

root.title("Pablo") #Cambiamos el titutlo de la ventana

root.resizable(0,True)#La ventana no abre a lo ancho --> 0 es false y 1 es true (podemos poner tambien las palabras)

#se puede cambiar tambien el logo con una imagen ico --> pagina para cambiar una img (https://convertio.co/es/jpg-ico/)

# root.geometry("600x300")#Cambiar la dimension


#un frame es una parte/o componente de la interface
#a continuacion esta como editarlo:
miframe = Frame(root)
miframe.pack()
miframe.pack(side=LEFT)
miframe.config(width=400, height=400)#cambiar dimensiones

miframe.config(cursor="pirate")#cambiar el cursor

miframe.config(bg="blue")#cambiar el color de fondo

#Para mas revisar la documnetacion de Python




root.mainloop()#aqui creamos un bucle que abre la ventana
