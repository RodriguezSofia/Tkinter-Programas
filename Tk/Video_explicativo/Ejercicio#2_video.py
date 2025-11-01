import tkinter #se importa solo el modulo tkinter
#si queremos utilizar todo lo que trae la libreria utilizamos form tkinter import *
ventana=tkinter.Tk() #se crea una ventana
ventana.geometry("400x300") #se define el tamaño de la ventana
def saludo(nombre):
    print("Hola "+ nombre)
boton1=tkinter.Button(ventana, text ="Presiona", command= lambda:saludo("Enrique"), padx=40,pady=40) #se crea un boton, padx=ancho, pady=alto, lambda para pasar parametros
boton1.pack() #nos permite ver el boton en la ventana
ventana.mainloop() 
