from Tkinter import *

root = Tk()

miFrame = Frame(root, width=500, height=400)

miFrame.pack()

miImagen=PhotoImage(file="fuck.gif")
Label(miFrame, image=miImagen).place(x=0, y=0)
"""Label(miFrame, text="Hola a Todos", fg = "green", font=("Verdana", 26)).place(x=100, y=200)"""

root.mainloop()