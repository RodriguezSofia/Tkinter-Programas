import tkinter as tk # Usamos tk como alias para mayor claridad

ventana = tk.Tk()
ventana.geometry("400x300")
ventana.title("Conversor de Temperaturas")
ventana.iconbitmap("Imagenes/conversor.ico")
# TITULO
etiqueta = tk.Label(ventana, text="Conversor de Temperaturas", fg="blue", font=("Arial", 16, " bold"))
etiqueta.pack()

# Entrada de grado
etiqueta_grados = tk.Label(ventana, text="Grados a convertir:", font=("Arial", 12))
etiqueta_grados.pack()
grados = tk.Entry(ventana, font=("Arial", 12))
grados.pack()

etiqueta_resultado = tk.Label(ventana, text="", fg="red", font=("Arial", 12, "italic"))#etiqueta para mostrar resultado


# CONVERSION
def convertir_a_celsius():
    try:# Manejo de errores para entradas que no sean numéricas
        fahrenheit = float(grados.get())
        celsius = (fahrenheit - 32) * 5/9
        nuevo_texto = f"{fahrenheit}°F son {celsius:.2f}°C" # .2f para 2 decimales
        etiqueta_resultado.config(text=nuevo_texto)
    except ValueError: # Captura el error si la conversión falla
        etiqueta_resultado.config(text="¡Lo siento! Por favor introduce un número válido.", fg="red")

def convertir_a_fahrenheit():
    try:
        celsius = float(grados.get())
        fahrenheit = (celsius * 9/5) + 32
        nuevo_texto = f"{celsius}°C son {fahrenheit:.2f}°F"
        etiqueta_resultado.config(text=nuevo_texto)
    except ValueError:
        etiqueta_resultado.config(text="¡Lo siento! Por favor introduce un número válido.", fg="red")

# BOTONES
boton_celsius = tk.Button(ventana, text="Convertir a Celsius", command=convertir_a_celsius, bg="lightblue")
boton_celsius.pack()
etiqueta_espacio = tk.Label(ventana, text="ó") # Etiqueta para espacio entre botones
etiqueta_espacio.pack()
boton_fahrenheit = tk.Button(ventana, text="Convertir a Fahrenheit", command=convertir_a_fahrenheit, bg="lightblue")
boton_fahrenheit.pack()
etiqueta_resultado.pack()

ventana.mainloop()