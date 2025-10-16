import tkinter
ventana=tkinter.Tk()
ventana.geometry("400x300")
ventana.title("Ejercicio 1")
#TITULO DEL FORMULARIO
etiqueta=tkinter.Label(ventana, text="Formulario de registro", fg="purple", font=("Arial", 16," bold"))
etiqueta.pack()
#CAMPOS DEL FORMULARIO: NOMBRE, EDAD, CORREO ELECTRONICO
#-------nombre--------
etiqueta_nombre=tkinter.Label(ventana, text="Nombre:", font=("Arial", 12))
etiqueta_nombre.pack()
nombre=tkinter.Entry(ventana,font=("Arial", 12))
nombre.pack()
#-------edad--------
etiqueta_edad=tkinter.Label(ventana, text="Edad:", font=("Arial", 12))
etiqueta_edad.pack()
edad=tkinter.Entry(ventana,font=("Arial", 12))
edad.pack()
#-------correo electronico--------
etiqueta_correo=tkinter.Label(ventana, text="Correo electronico:", font=("Arial", 12))
etiqueta_correo.pack()
correo=tkinter.Entry(ventana,font=("Arial", 12))
correo.pack()
#INFORMACION
def info_guardada():
    nombre_guardado=nombre.get()
    edad_guardada=edad.get() 
    correo_guardado=correo.get()
    etiqueta_info=tkinter.Label(ventana, text=f"Nombre: {nombre_guardado}, Edad: {edad_guardada}, Correo: {correo_guardado}", fg="green", font=("Arial", 12, "italic"))
    etiqueta_info.pack()
#BOTON "GUARDAR"
boton=tkinter.Button(ventana, text="Guardar", command= info_guardada)
boton.pack()
ventana.mainloop()
