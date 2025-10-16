import tkinter
ventana=tkinter.Tk()
ventana.geometry("400x300")
ventana.title("Ejercicio 2")
#TITULO
etiqueta=tkinter.Label(ventana, text="Conversor de Temperaturas", fg="blue", font=("Arial", 16," bold"))
etiqueta.pack()

#Entrada de grado 
etiqueta_grados=tkinter.Label(ventana, text="Grados a convertir:", font=("Arial", 12))
etiqueta_grados.pack()
grados=tkinter.Entry(ventana,font=("Arial", 12))
grados.pack()

#CONVERSION
def convertir_a_celsius():
    fahrenheit=float(grados.get())
    celsius=(fahrenheit - 32) * 5/9
    etiqueta_resultado1=tkinter.Label(ventana, text=f"{fahrenheit}°F son {celsius}°C", fg="red", font=("Arial", 12, "italic"))
    etiqueta_resultado1.pack()

def convertir_a_fahrenheit():
    celsius=float(grados.get())
    fahrenheit=(celsius * 9/5) + 32
    etiqueta_resultado2=tkinter.Label(ventana, text=f"{celsius}°C son {fahrenheit}°F", fg="red", font=("Arial", 12, "italic"))
    etiqueta_resultado2.pack()

#BOTONES
boton_celsius=tkinter.Button(ventana, text="Convertir a Celsius", command= convertir_a_celsius, bg="lightblue")
boton_celsius.pack()
etiqueta_espacio=tkinter.Label(ventana, text="ó") #Etiqueta para espacio entre botones
etiqueta_espacio.pack()
boton_fahrenheit=tkinter.Button(ventana, text="Convertir a Fahrenheit", command= convertir_a_fahrenheit, bg="lightblue")
boton_fahrenheit.pack()


ventana.mainloop()