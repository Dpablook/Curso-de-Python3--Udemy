from tkinter import *

root = Tk()
root.title("Check Button")

frame = Frame(root)
frame.pack()

checkbutton(frame, text="Nombre", variable="opcion1", onvalue=1, offvalue=0).pack()
checkbutton(frame, text="Nombre", variable="opcion2", onvalue=0, offvalue=1).pack()

root.mainloop()