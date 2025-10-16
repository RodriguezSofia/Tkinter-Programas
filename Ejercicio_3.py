import tkinter
ventana=tkinter.Tk()
ventana.geometry("600x400")
ventana.title("Ejercicio 3")
#TITULO
etiqueta=tkinter.Label(ventana, text="Lista de tareas", fg="red", font=("Arial", 16," bold"))
etiqueta.pack()

#Entrada de tarea
etiqueta_tarea=tkinter.Label(ventana, text="Tarea a agregar:", font=("Arial", 12))
etiqueta_tarea.pack()
tarea=tkinter.Entry(ventana,font=("Arial", 12))
tarea.pack()

#LISTA DE TAREAS
titulo_lista=tkinter.Label(ventana, text="Tareas:", font=("Arial", 12, "bold"))
titulo_lista.pack()
lista_tareas=tkinter.Listbox(ventana, font=("Arial", 12), width=40, height=10)
lista_tareas.pack()

#AGREGAR TAREA
def agregar_tarea():
    nueva_tarea=tarea.get()
    if nueva_tarea.strip() != "":
        lista_tareas.insert(tkinter.END, nueva_tarea)
        tarea.delete(0, tkinter.END)

#ELIMINAR TAREA
def eliminar_tarea():
    tarea_seleccionada=lista_tareas.curselection()
    if tarea_seleccionada:
        lista_tareas.delete(tarea_seleccionada)

#BOTON "ELIMINAR"
boton_eliminar=tkinter.Button(ventana, text="Eliminar", command= eliminar_tarea, bg="lightcoral", padx=10, pady=5)
boton_eliminar.pack()

#BOTON "AGREGAR"
boton_agregar=tkinter.Button(ventana, text="Agregar", command= agregar_tarea, bg="lightgreen", padx=30,pady=5)
boton_agregar.pack()

ventana.mainloop()