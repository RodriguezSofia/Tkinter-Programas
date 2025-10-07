import tkinter as tk 
#-------------FUNCIONES----------------
def sumar():
    try:
        n1 = float(entrada1.get())
        n2 = float(entrada2.get())
        resultado.set(n1 + n2)
    except ValueError:
        resultado.set("Error")
#-------------VENTANA PRINCIPAL----------------
ventana = tk.Tk()
ventana.title("Calculadora básica")
ventana.geometry("250x180") #tamaño de la ventana
#-------------VARIABLE----------------
resultado = tk.StringVar()
#-------------WIDGETS----------------
tk.Label(ventana, text="Número 1:").pack(pady=5)
entrada1 = tk.Entry(ventana)
entrada1.pack()

tk.Label(ventana, text="Número 2:").pack(pady=5)
entrada2 = tk.Entry(ventana)
entrada2.pack()

tk.Button(ventana, text="Sumar", command=sumar).pack(pady=5)
tk.Label(ventana, text="Resultado:").pack()
tk.Label(ventana, textvariable=resultado, fg="blue", font=("Arial 12")).pack()
#-------------LOOP PRINCIPAL----------------
ventana.mainloop()