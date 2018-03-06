from Tkinter import *

raiz = Tk()
miFrame = Frame()

raiz.title("Ventana de Pruebas") #Darle un titulo a la ventana
#raiz.resizable(1, 0) #Impide redimensionar una ventana
raiz.iconbitmap("Arqueros_Historicos.ico") #Pone una imagen en la barra del titulo de la ventana
#raiz.geometry("650x350") #Redimensiona el tamanio de la ventana
raiz.config(bg="green") #Personaliza la ventana

miFrame.pack()
miFrame.config(bg="red", width="650", height="350", bd="35", relief="groove", cursor="pirate")
raiz.mainloop() #Lanza una ventana