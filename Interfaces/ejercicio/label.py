#Label

from tkinter import *



root=Tk()
root.title("Bienvenidos")
root.config(width=400,height=300)
#como manipular una etiqueta:
#

label = Label(root, text="Hola")
label.place(x=100,y=50) #Importante recordar empaquetar
label.config(bg="light cyan",fg="red") #Hay una pagina que se llama coores tkinter (http://www.science.smith.edu/dftwiki/index.php/Color_Charts_for_TKinter)

Label(root, text="Bienvenidos").place(x=15,y=25) #Aqui el problema es que no podemos usar el config
#esto sirve si luego no se va a modificar



root.mainloop()