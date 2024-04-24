import os
import tkinter as tk
from tkinter import messagebox
from pyswip import Prolog

# Funciones
prolog = Prolog()
prolog.consult("Prolog.pl")

def comprobar_mamifero():
    animal = entrada_animal.get().lower()
    es_mamifero=bool(list(prolog.query("es_mamifero("+animal+")")))
    if es_mamifero:
        messagebox.showinfo("Resultado", f"El animal {animal} es un mamífero.")
    else:
        messagebox.showerror("Resultado", f"El animal {animal} no es un mamífero.")  
    


def comprobar_ave():
    animal = entrada_animal.get().lower()
    es_ave=bool(list(prolog.query("es_ave("+animal+")")))
    if es_ave:
       messagebox.showinfo("Resultado", f"El animal {animal} es un ave.")
    else:
       messagebox.showerror("Resultado", f"El animal {animal} no es un ave.")

#Interfaz
ventana = tk.Tk()
ventana.title("ANIMAL")
ventana.geometry("200x180")
ventana.resizable(0,0)


etiqueta_animal = tk.Label(ventana, text="Nombre del animal:", pady=2)
etiqueta_animal.pack()
entrada_animal = tk.Entry(ventana)
entrada_animal.pack()
espaciado = tk.Frame(ventana, height=10)
espaciado.pack()

boton_mamifero = tk.Button(ventana, text="Comprobar si es mamífero", command=comprobar_mamifero, pady=2)
boton_mamifero.pack()
espaciado = tk.Frame(ventana, height=10)
espaciado.pack()
boton_ave = tk.Button(ventana, text="Comprobar si es ave", command=comprobar_ave, pady=2)
boton_ave.pack()
espaciado = tk.Frame(ventana, height=10)
espaciado.pack()
boton_salir = tk.Button(ventana, text="Salir", command=ventana.quit, pady=2)
boton_salir.pack()

ventana.mainloop()
