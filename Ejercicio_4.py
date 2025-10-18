import tkinter
ventana=tkinter.Tk()
ventana.geometry("400x300")
ventana.title("Ejercicio 4")
ventana.iconbitmap("Imagenes/cursor.ico")
#TITULO
etiqueta=tkinter.Label(ventana, text="Contador de cliks", fg="blue", font=("Arial", 18," bold"))
etiqueta.pack()
#CONTADOR
contador=0
etiqueta_contador=tkinter.Label(ventana, text=f"Número de clicks: {contador}", fg="green", font=("Arial", 12))
#FUNCION INCREMENTAR CONTADOR
def incrementar_contador():
    global contador
    contador += 1
    etiqueta_contador.config(text=f"Número de clicks: {contador}")

#BOTON
boton=tkinter.Button(ventana, text="¡Haz Click!", font=("Arial", 12), command= incrementar_contador, bg="lightblue", padx=20, pady=10)
boton.pack()
etiqueta_contador.pack()
ventana.mainloop()