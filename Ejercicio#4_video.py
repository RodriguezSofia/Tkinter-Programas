import tkinter #se importa solo el modulo tkinter
#si queremos utilizar todo lo que trae la libreria utilizamos form tkinter import *
ventana=tkinter.Tk() #se crea una ventana
ventana.geometry("400x300") #se define el tamaño de la ventana
#metodo grid ayuda a posicionar nustros widgets
boton1=tkinter.Button(ventana, text="boton 1",width=10, height=5)
boton2=tkinter.Button(ventana, text="boton 2",width=10, height=5)
boton3=tkinter.Button(ventana, text="boton 3",width=10, height=5)

boton1.grid(row=0, column=0) #row=fila, column=columna
boton2.grid(row=1, column=0)
boton3.grid(row=2, column=0)
ventana.mainloop() #lleva el registro de lo que sucede en la ventana
