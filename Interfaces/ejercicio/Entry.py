#Entry
#una input para ingresar datos


from tkinter import *

root=Tk()
root.title("Entry")

frame = Frame(root,width=40, height=400)#Creasmos un frame
frame.pack()

entrada = Entry(frame)#Luego creamos el Entry
entrada.grid(row=0, column=1)#para acomodarlos

label1 = Label(frame, text="Nombre")
label1.grid(row=0, column=0, sticky="n")#Para moverlo al centro

#segundo Entry
entrada2 = Entry(frame)
entrada2.grid(row=1, column=1)

label2 = Label(frame, text="Apellido")
label2.grid(row=1, column=0)

root.mainloop()