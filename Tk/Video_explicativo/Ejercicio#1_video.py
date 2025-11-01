import tkinter #se importa solo el modulo tkinter
#si queremos utilizar todo lo que trae la libreria utilizamos form tkinter import *
ventana=tkinter.Tk() #se crea una ventana
ventana.geometry("400x300") #se define el tamaño de la ventana
#_____elementos de la ventana_____
etiqueta=tkinter.Label(ventana, text="Hola mundo", bg="purple")
etiqueta.pack(fill=tkinter.BOTH, expand=True) #nos permite ver la etiqueta en la ventana, Fill=LLENAR, SIDE=POSICIONAR
ventana.mainloop() #lleva el registro de lo que sucede en la ventana
#el mainloop es un ciclo infinito que mantiene la ventana abierta