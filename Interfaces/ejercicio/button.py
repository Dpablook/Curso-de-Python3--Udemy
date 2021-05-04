#Button
#

#Se crean de esa forma:
#
# boton1 = Button(frame, text="Enviar")#creamos un boton
# boton1.pack()
#


from tkinter import *

def sumar():
	resultado.set(int(var1.get())+ int(var2.get()))

def restar():
	resultado.set(int(var1.get())- int(var2.get()))

def multiplicar():
	resultado.set(int(var1.get())* int(var2.get()))

def dividir():
	resultado.set(int(var1.get())/ int(var2.get()))

root = Tk()
root.title("Button")


frame = Frame(root)
frame.pack()

var1= StringVar()
var2= StringVar()
resultado= StringVar()

#Calculadora - Practica:
#
entrada1 = Entry(frame)
entrada1.pack()
entrada1.config(bd=10, font=("Curier 20"), textvariable=var1)

entrada2 = Entry(frame)
entrada2.pack()
entrada2.config(bd=10, font=("Curier 20"), textvariable=var2)

entrada3 = Entry(frame)
entrada3.pack()
entrada3.config(bd=10, font=("Curier 20"), state="disable", textvariable=resultado) #Con esto no se puede manipular

boton1 = Button(frame, text="Sumar")
boton1.pack()
boton1.config(bd=5, font=("Curier 10"), command=sumar)#con esto llamamos a la funcion sumar

boton2 = Button(frame, text="Restar")
boton2.pack()
boton2.config(bd=5, font=("Curier 10"), command=restar)

boton3 = Button(frame, text="Multiplicar")
boton3.pack()
boton3.config(bd=5, font=("Curier 10"), command=multiplicar)#con esto llamamos a la funcion sumar

boton4 = Button(frame, text="Dividir")
boton4.pack()
boton4.config(bd=5, font=("Curier 10"), command=dividir)


root.mainloop()