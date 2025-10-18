import tkinter
ventana=tkinter.Tk()
ventana.geometry("600x400")
ventana.title("Lista de Tareas")
ventana.iconbitmap("Imagenes/libreta.ico")
ventana.configure(bg="lightyellow")
#Titulo
etiqueta=tkinter.Label(ventana, text="Lista de tareas", fg="darkred", bg="lightyellow", font=("Arial", 16," bold"))
etiqueta.pack()

#Entrada de tarea
etiqueta_tarea=tkinter.Label(ventana, text="Tarea a agregar:", bg="lightyellow", font=("Arial", 12))
etiqueta_tarea.pack()
tarea=tkinter.Entry(ventana,font=("Arial", 12))
tarea.pack()

#Lista de tareas
etiqueta_lista=tkinter.Label(ventana, text="Tareas:", bg="lightyellow", font=("Arial", 12, "bold"))
etiqueta_lista.pack()
lista_tareas=tkinter.Listbox(ventana, font=("Arial", 12), width=40, height=10)
lista_tareas.pack() #Listbox sirve para crear listas

#---------FUNCIONES---------
#Agregar tarea
def agregar_tarea():
    nueva_tarea=tarea.get()
    lista_tareas.insert(tkinter.END, nueva_tarea) #insertar al final en la lista
    tarea.delete(0, tkinter.END) #para limpiar la entrada despues de agregar
#Eliminar tarea
def eliminar_tarea():
    tarea_seleccionada=lista_tareas.curselection() #para obtener la tarea seleccionada con el cursor
    lista_tareas.delete(tarea_seleccionada) #elimina la tarea seleccionada

#---------BOTONES---------
#Boton "AGREGAR"
boton_agregar=tkinter.Button(ventana, text="Agregar", fg="green", font= ("Arial", 12, "bold" ), command= agregar_tarea, bg="lightgreen", padx=30,pady=5)
boton_agregar.pack()
#Boton "ELIMINAR"
boton_eliminar=tkinter.Button(ventana, text="Eliminar", fg="red", font= ("Arial", 12, "bold" ), command= eliminar_tarea, bg="lightcoral", padx=30, pady=5)
boton_eliminar.pack()

ventana.mainloop()