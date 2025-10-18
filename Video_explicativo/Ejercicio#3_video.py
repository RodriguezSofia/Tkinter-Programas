import tkinter #se importa solo el modulo tkinter
#si queremos utilizar todo lo que trae la libreria utilizamos form tkinter import *
ventana=tkinter.Tk() #se crea una ventana
ventana.geometry("400x300") #se define el tamaño de la ventana
cajaTexto=tkinter.Entry(ventana, font="Helvetica 15") #crea una caja de texto
cajaTexto.pack() 
etiqueta = tkinter.Label(ventana)
etiqueta.pack()
def textoDeLaCaja():
    text20 =cajaTexto.get()#get obtiene el texto que se escribe en la caja de texto
    etiqueta["text"]= text20
boton=tkinter.Button(ventana, text="Enviar", command=textoDeLaCaja)
boton.pack()
ventana.mainloop() #lleva el registro de lo que sucede en la ventana
