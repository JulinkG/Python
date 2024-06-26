import tkinter as tk
from tkinter import ttk
import mysql.connector 
from datetime import datetime

class InterfazCandidatos:
    def __init__(self, master):
        self.master = master
        self.master.title("Gestión de Candidatos")

        # Tenemos que conectar la base de datos o crearla en SQL, en este caso vamos a crearta desde cero
        self.conn = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='JulinkR00t',
        database='crud_python'
        )

        self.conn.cursor().execute('''
    CREATE TABLE IF NOT EXISTS candidatos (
    idCandidatos INT AUTO_INCREMENT PRIMARY KEY,
    Fecha_ingreso_datos DATETIME NOT NULL,
    Nombre VARCHAR(255) NOT NULL,
    Edad INT,
    Escolaridad VARCHAR(255),
    Rubro VARCHAR(255),
    Ubicacion VARCHAR(255),
    Reubicacion VARCHAR(255),
    Estado_civil VARCHAR(255),
    Discapacidad_enfermedad VARCHAR(255),
    Hijos INT,
    Telefono VARCHAR(255),
    correo VARCHAR(255)
    )
    ''')

        self.create_widgets()

    def create_widgets(self):
        # Etiquetas y cuadros de texto
        self.label_nombre = ttk.Label(self.master, text="Nombre:")
        self.label_nombre.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        self.entry_nombre = ttk.Entry(self.master)
        self.entry_nombre.grid(row=0, column=1, padx=5, pady=5)

        self.label_edad = ttk.Label(self.master, text="Edad:")
        self.label_edad.grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        self.entry_edad = ttk.Entry(self.master)
        self.entry_edad.grid(row=1, column=1, padx=5, pady=5)

        self.label_escolaridad = ttk.Label(self.master, text="Escolaridad:")
        self.label_escolaridad.grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
        self.entry_escolaridad = ttk.Entry(self.master)
        self.entry_escolaridad.grid(row=2, column=1, padx=5, pady=5)

        self.label_rubro = ttk.Label(self.master, text="Rubro:")
        self.label_rubro.grid(row=3, column=0, sticky=tk.W, padx=5, pady=5)
        self.entry_rubro = ttk.Entry(self.master)
        self.entry_rubro.grid(row=3, column=1, padx=5, pady=5)

        self.label_ubicacion = ttk.Label(self.master, text="Ubicacion:")
        self.label_ubicacion.grid(row=4, column=0, sticky=tk.W, padx=5, pady=5)
        self.entry_ubicacion = ttk.Entry(self.master)
        self.entry_ubicacion.grid(row=4, column=1, padx=5, pady=5)

        self.label_reubicacion = ttk.Label(self.master, text="Reubicacion:")
        self.label_reubicacion.grid(row=5, column=0, sticky=tk.W, padx=5, pady=5)
        self.entry_reubicacion = ttk.Entry(self.master)
        self.entry_reubicacion.grid(row=5, column=1, padx=5, pady=5)

        self.label_estado_civil = ttk.Label(self.master, text="Estado Civil:")
        self.label_estado_civil.grid(row=6, column=0, sticky=tk.W, padx=5, pady=5)
        self.entry_estado_civil = ttk.Entry(self.master)
        self.entry_estado_civil.grid(row=6, column=1, padx=5, pady=5)

        self.label_discapacidad = ttk.Label(self.master, text="Discapacidad/Enfermedad:")
        self.label_discapacidad.grid(row=7, column=0, sticky=tk.W, padx=5, pady=5)
        self.entry_discapacidad = ttk.Entry(self.master)
        self.entry_discapacidad.grid(row=7, column=1, padx=5, pady=5)

        self.label_hijos = ttk.Label(self.master, text="Número de Hijos:")
        self.label_hijos.grid(row=8, column=0, sticky=tk.W, padx=5, pady=5)
        self.entry_hijos = ttk.Entry(self.master)
        self.entry_hijos.grid(row=8, column=1, padx=5, pady=5)

        self.label_telefono = ttk.Label(self.master, text="Teléfono:")
        self.label_telefono.grid(row=9, column=0, sticky=tk.W, padx=5, pady=5)
        self.entry_telefono = ttk.Entry(self.master)
        self.entry_telefono.grid(row=9, column=1, padx=5, pady=5)

        self.label_correo = ttk.Label(self.master, text="Correo:")
        self.label_correo.grid(row=10, column=0, sticky=tk.W, padx=5, pady=5)
        self.entry_correo = ttk.Entry(self.master)
        self.entry_correo.grid(row=10, column=1, padx=5, pady=5)

        # Botones
        self.btn_agregar = ttk.Button(self.master, text="Agregar Candidato", command=self.agregar_candidato)
        self.btn_agregar.grid(row=11, column=0, columnspan=2, pady=10)

        self.btn_visualizar = ttk.Button(self.master, text="Visualizar Candidatos", command=self.visualizar_candidatos)
        self.btn_visualizar.grid(row=12, column=0, columnspan=2, pady=10)

        self.btn_editar = ttk.Button(self.master, text="Editar Candidato", command=self.editar_candidato)
        self.btn_editar.grid(row=13, column=0, columnspan=2, pady=10)

        self.label_rubro = ttk.Label(self.master, text="Filtrar por Rubro:")
        self.label_rubro.grid(row=14, column=0, padx=5, pady=5, sticky=tk.W)

        self.combo_rubro = ttk.Combobox(self.master, values=["", "IT", "Marketing", "Ventas", "Recursos Humanos"])
        self.combo_rubro.grid(row=14, column=1, padx=5, pady=5, sticky=tk.W)
        self.combo_rubro.set("")  # Establecer un valor predeterminado

        # Botón para aplicar el filtrado
        ttk.Button(self.master, text="Filtrar", command=self.filtrar_candidatos).grid(row=14, column=2, padx=5, pady=5)

        # Salida
        self.text_salida = tk.Text(self.master, height=10, width=80)
        self.text_salida.grid(row=15, column=0, columnspan=2, pady=10)

    def filtrar_candidatos(self):
        # Limpiar el área de salida
        self.text_salida.delete('1.0', tk.END)

        # Obtener el rubro seleccionado
        rubro_seleccionado = self.combo_rubro.get()

        # Construir la consulta SQL con el filtro de rubro
        query = 'SELECT * FROM candidatos'
        if rubro_seleccionado:
            query += f" WHERE Rubro = '{rubro_seleccionado}'"

        # Ejecutar la consulta
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute(query)

        # Mostrar los resultados en el área de salida
        for row in cursor.fetchall():
            mensaje = f"ID: {row['idCandidatos']}, Nombre: {row['Nombre']}, Edad: {row['Edad']}, Escolaridad: {row['Escolaridad']}, Rubro: {row['Rubro']}, Ubicacion: {row['Ubicacion']}, Reubicacion: {row['Reubicacion']}, Estado Civil: {row['Estado_civil']}, Discapacidad/Enfermedad: {row['Discapacidad_enfermedad']}, Hijos: {row['Hijos']}, Telefono: {row['Telefono']}, Correo: {row['correo']}, Fecha Ingreso: {row['Fecha_ingreso_datos']}\n"
            self.text_salida.insert(tk.END, mensaje)


    def filtrar_candidatos(self):
        # Limpiar el área de salida
        self.text_salida.delete('1.0', tk.END)

        # Obtener el rubro seleccionado
        rubro_seleccionado = self.combo_rubro.get()

        # Construir la consulta SQL con el filtro de rubro
        query = 'SELECT * FROM candidatos'
        if rubro_seleccionado:
            query += f" WHERE Rubro = '{rubro_seleccionado}'"

        # Ejecutar la consulta
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute(query)

        # Mostrar los resultados en el área de salida
        for row in cursor.fetchall():
            mensaje = f"ID: {row['idCandidatos']}, Nombre: {row['Nombre']}, Edad: {row['Edad']}, Escolaridad: {row['Escolaridad']}, Rubro: {row['Rubro']}, Ubicacion: {row['Ubicacion']}, Reubicacion: {row['Reubicacion']}, Estado Civil: {row['Estado_civil']}, Discapacidad/Enfermedad: {row['Discapacidad_enfermedad']}, Hijos: {row['Hijos']}, Telefono: {row['Telefono']}, Correo: {row['correo']}, Fecha Ingreso: {row['Fecha_ingreso_datos']}\n"
            self.text_salida.insert(tk.END, mensaje)

    def agregar_candidato(self):
        nombre = self.entry_nombre.get()
        edad = int(self.entry_edad.get()) if self.entry_edad.get() else None
        escolaridad = self.entry_escolaridad.get()
        rubro = self.entry_rubro.get()
        ubicacion = self.entry_ubicacion.get()
        reubicacion = self.entry_reubicacion.get()
        estado_civil = self.entry_estado_civil.get()
        discapacidad = self.entry_discapacidad.get()
        hijos = int(self.entry_hijos.get()) if self.entry_hijos.get() else None
        telefono = self.entry_telefono.get()
        correo = self.entry_correo.get()
        self.entry_nombre.delete(0, tk.END)
        self.entry_edad.delete(0, tk.END)
        self.entry_escolaridad.delete(0, tk.END)
        self.entry_rubro.delete(0, tk.END)
        self.entry_ubicacion.delete(0, tk.END)
        self.entry_reubicacion.delete(0, tk.END)
        self.entry_estado_civil.delete(0, tk.END)
        self.entry_discapacidad.delete(0, tk.END)
        self.entry_hijos.delete(0, tk.END)
        self.entry_telefono.delete(0, tk.END)
        self.entry_correo.delete(0, tk.END)

        fecha_ingreso = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Agregar el candidato a la base de datos
        self.conn.cursor().execute('''
        INSERT INTO candidatos (
            Fecha_ingreso_datos, Nombre, Edad, Escolaridad, Rubro, Ubicacion, 
            Reubicacion, Estado_civil, Discapacidad_enfermedad, Hijos, Telefono, correo
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        ''', (fecha_ingreso, nombre, edad, escolaridad, rubro, ubicacion, reubicacion, estado_civil, discapacidad, hijos, telefono, correo))
        self.conn.commit()

        mensaje = f'Candidato {nombre} agregado con éxito.'
        self.text_salida.insert(tk.END, mensaje + '\n')

    def visualizar_candidatos(self):
        # Limpiar el área de salida
        self.text_salida.delete('1.0', tk.END)

        # Obtener datos de la base de datos
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM candidatos')
        rows = cursor.fetchall()

        for row in rows:
            mensaje = f"ID: {row[0]}, Nombre: {row[2]}, Edad: {row[3]}, Escolaridad: {row[4]}, Rubro: {row[5]}, Ubicacion: {row[6]}, Reubicacion: {row[7]}, Estado Civil: {row[8]}, Discapacidad/Enfermedad: {row[9]}, Hijos: {row[10]}, Telefono: {row[11]}, Correo: {row[12]}, Fecha Ingreso: {row[1]}\n"
            self.text_salida.insert(tk.END, mensaje)

    def editar_candidato(self):
        # Ventana de edición
        ventana_editar = tk.Toplevel(self.master)
        ventana_editar.title("Editar Candidato")

        # Etiquetas y cuadros de texto para la edición
        ttk.Label(ventana_editar, text="ID del Candidato:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        entry_id = ttk.Entry(ventana_editar)
        entry_id.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(ventana_editar, text="Nuevo Nombre:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        entry_nuevo_nombre = ttk.Entry(ventana_editar)
        entry_nuevo_nombre.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(ventana_editar, text="Nueva Edad:").grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
        entry_nueva_edad = ttk.Entry(ventana_editar)
        entry_nueva_edad.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(ventana_editar, text="Nueva Escolaridad:").grid(row=3, column=0, sticky=tk.W, padx=5, pady=5)
        entry_nueva_escolaridad = ttk.Entry(ventana_editar)
        entry_nueva_escolaridad.grid(row=3, column=1, padx=5, pady=5)

        ttk.Label(ventana_editar, text="Nuevo Rubro:").grid(row=4, column=0, sticky=tk.W, padx=5, pady=5)
        entry_nuevo_rubro = ttk.Entry(ventana_editar)
        entry_nuevo_rubro.grid(row=4, column=1, padx=5, pady=5)

        ttk.Label(ventana_editar, text="Nueva Ubicacion:").grid(row=5, column=0, sticky=tk.W, padx=5, pady=5)
        entry_nueva_ubicacion = ttk.Entry(ventana_editar)
        entry_nueva_ubicacion.grid(row=5, column=1, padx=5, pady=5)

        ttk.Label(ventana_editar, text="Nueva Reubicacion:").grid(row=6, column=0, sticky=tk.W, padx=5, pady=5)
        entry_nueva_reubicacion = ttk.Entry(ventana_editar)
        entry_nueva_reubicacion.grid(row=6, column=1, padx=5, pady=5)

        ttk.Label(ventana_editar, text="Nuevo Estado Civil:").grid(row=7, column=0, sticky=tk.W, padx=5, pady=5)
        entry_nuevo_estado_civil = ttk.Entry(ventana_editar)
        entry_nuevo_estado_civil.grid(row=7, column=1, padx=5, pady=5)

        ttk.Label(ventana_editar, text="Nueva Discapacidad/Enfermedad:").grid(row=8, column=0, sticky=tk.W, padx=5, pady=5)
        entry_nueva_discapacidad = ttk.Entry(ventana_editar)
        entry_nueva_discapacidad.grid(row=8, column=1, padx=5, pady=5)

        ttk.Label(ventana_editar, text="Nuevo Número de Hijos:").grid(row=9, column=0, sticky=tk.W, padx=5, pady=5)
        entry_nuevo_hijos = ttk.Entry(ventana_editar)
        entry_nuevo_hijos.grid(row=9, column=1, padx=5, pady=5)

        ttk.Label(ventana_editar, text="Nuevo Teléfono:").grid(row=10, column=0, sticky=tk.W, padx=5, pady=5)
        entry_nuevo_telefono = ttk.Entry(ventana_editar)
        entry_nuevo_telefono.grid(row=10, column=1, padx=5, pady=5)

        ttk.Label(ventana_editar, text="Nuevo Correo:").grid(row=11, column=0, sticky=tk.W, padx=5, pady=5)
        entry_nuevo_correo = ttk.Entry(ventana_editar)
        entry_nuevo_correo.grid(row=11, column=1, padx=5, pady=5)

        # Función para aplicar la edición
        def aplicar_edicion():
            candidato_id = entry_id.get()
            nuevo_nombre = entry_nuevo_nombre.get()
            nueva_edad = int(entry_nueva_edad.get()) if entry_nueva_edad.get() else None
            nueva_escolaridad = entry_nueva_escolaridad.get()
            nuevo_rubro = entry_nuevo_rubro.get()
            nueva_ubicacion = entry_nueva_ubicacion.get()
            nueva_reubicacion = entry_nueva_reubicacion.get()
            nuevo_estado_civil = entry_nuevo_estado_civil.get()
            nueva_discapacidad = entry_nueva_discapacidad.get()
            nuevo_hijos = int(entry_nuevo_hijos.get()) if entry_nuevo_hijos.get() else None
            nuevo_telefono = entry_nuevo_telefono.get()
            nuevo_correo = entry_nuevo_correo.get()

            # Actualizar datos en la base de datos
            self.conn.cursor().execute('''
            UPDATE candidatos
            SET Nombre=%s, Edad=%s, Escolaridad=%s, Rubro=%s, Ubicacion=%s, 
                Reubicacion=%s, Estado_civil=%s, Discapacidad_enfermedad=%s, 
                Hijos=%s, Telefono=%s, correo=%s
            WHERE idCandidatos=%s
            ''', (nuevo_nombre, nueva_edad, nueva_escolaridad, nuevo_rubro, nueva_ubicacion,
                  nueva_reubicacion, nuevo_estado_civil, nueva_discapacidad,
                  nuevo_hijos, nuevo_telefono, nuevo_correo, candidato_id))
            self.conn.commit()

            mensaje = f'Datos del Candidato ID {candidato_id} actualizados con éxito.'
            self.text_salida.insert(tk.END, mensaje + '\n')

            # Cerrar la ventana de edición
            ventana_editar.destroy()

        # Botón para aplicar la edición
        ttk.Button(ventana_editar, text="Aplicar Edición", command=aplicar_edicion).grid(row=12, column=0, columnspan=2, pady=10)

    def cerrar_ventana(self):
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = InterfazCandidatos(root)
    root.protocol("WM_DELETE_WINDOW", app.cerrar_ventana)  # Configurar el botón de cerrar para cerrar la conexión a la base de datos
    root.mainloop()

# Cerrar la conexión a la base de datos al final del programa
app.conn.close()
