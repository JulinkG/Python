import tkinter as tk
from tkinter import messagebox

# Definimos nuestra función principal
def calcular_comision():
    try:
        nombre = nombre_entry.get()
        monto = float(monto_entry.get())
        porcentaje = float (porcentaje_comision_entry.get())

        comision_calculada = monto * (porcentaje / 100)

        messagebox.showinfo("Resultado",f"Hola {nombre}, su comisión del més actual es de: {comision_calculada:.2f}$.")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese valores numéricos válidos.")


# Creamos una ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de comisiones")

# creamos las etiquetas
tk.Label(ventana, text= "Nombre:").grid(row=0, column=0, sticky="w", padx=10, pady=5)
tk.Label(ventana, text= "Monto total de ventas en pesos mexicanos:").grid(row=1, column=0, sticky="w", padx=10, pady=5)
tk.Label(ventana, text= "Porcentaje de comisión:").grid(row=2, column=0, sticky="w", padx=10, pady=5)

# Creamos las entradas de texto
nombre_entry= tk.Entry(ventana)
nombre_entry.grid(row=0, column=1, padx=10, pady=5)
monto_entry= tk.Entry(ventana)
monto_entry.grid(row=1, column=1, padx=10, pady=5)
porcentaje_comision_entry= tk.Entry(ventana)
porcentaje_comision_entry.grid(row=2, column=1, padx=10, pady=5)

# Configuramos el botón de calculo
boton = tk.Button(ventana, text="Calcular comision", command=calcular_comision) 
boton.grid(row=3, column=0, columnspan=2, pady=10)

# Iniciamos el bucle principal
ventana.mainloop()
