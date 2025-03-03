import tkinter as tk
from tkinter import ttk, messagebox
from DataBase import Database
from config_manager import ConfigManager


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Base de Datos")
        self.root.geometry("500x400")

        self.config = ConfigManager()
        self.db = None
        self.registros = []
        self.indice_actual = 0

        # Pantalla de Selección
        self.frame_seleccion = ttk.Frame(self.root)
        self.frame_seleccion.pack(pady=20)

        ttk.Label(self.frame_seleccion,
                  text="Seleccione Base de Datos:").pack()
        self.entry_db = ttk.Entry(self.frame_seleccion)
        self.entry_db.pack(pady=5)
        self.entry_db.insert(0, self.config.get_database_config()["database"])

        ttk.Label(self.frame_seleccion, text="Seleccione Tabla:").pack()
        self.entry_table = ttk.Entry(self.frame_seleccion)
        self.entry_table.pack(pady=5)

        ttk.Button(self.frame_seleccion, text="Cargar",
                   command=self.iniciar_gestion).pack(pady=10)

    def iniciar_gestion(self):
        """ Carga la base de datos y la tabla seleccionada """
        nueva_db = self.entry_db.get()
        nueva_tabla = self.entry_table.get()

        if not nueva_db or not nueva_tabla:
            messagebox.showerror(
                "Error", "Debe ingresar la base de datos y la tabla.")
            return

        self.config.set_database(nueva_db)
        self.db = Database(nueva_tabla)

        # 🔹 Ocultar la pantalla de selección y mostrar formulario
        self.frame_seleccion.pack_forget()
        self.crear_formulario(nueva_tabla)

    def crear_formulario(self, tabla):
        """ Crea el formulario con campos de entrada """
        self.frame_gestion = ttk.Frame(self.root)
        self.frame_gestion.pack(pady=10)

        ttk.Label(self.frame_gestion,
                  text=f"📋 Gestión de {tabla}", font=("Arial", 14)).pack()


        # 🔹 Cargar registros
        if tabla=="libros":
            self.cargar_registros_libros()
        else:
            self.cargar_registros()

        if not self.registros:
            messagebox.showerror(
                "Error", "No se encontraron registros en la tabla.")
            return

        self.campos = {}
        self.columnas = list(self.registros[0].keys())

        # Crear un subframe para los campos
        form_frame = ttk.Frame(self.frame_gestion)
        form_frame.pack()

        for columna in self.columnas:
            # Contenedor de cada fila (etiqueta + campo)
            frame_fila = ttk.Frame(form_frame)
            frame_fila.pack(pady=5, fill="x")
            if columna.lower() != "id":
                col = columna

                ttk.Label(frame_fila, text=col, width=15,
                          anchor="w").pack(side="left", padx=5)
             
                self.campos[col] = ttk.Entry(frame_fila)
                self.campos[col].pack(side="left", expand=True, fill="x")
                print (frame_fila)


        self.mostrar_registro()

        # 🔹 Botones de navegación y edición
        btn_frame = ttk.Frame(self.frame_gestion)
        btn_frame.pack(pady=10)

        ttk.Button(btn_frame, text="Anterior",
                   command=self.anterior_registro).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Siguiente",
                   command=self.siguiente_registro).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Modificar Registro",
                   command=self.modificar_registro).pack(pady=5)
        ttk.Button(btn_frame, text="Eliminar Registro",
                   command=self.eliminar_registro).pack(pady=5)
        ttk.Button(btn_frame, text="Nuevo Registro",
                   command=self.abrir_formulario_nuevo).pack(pady=5)

    def cargar_registros(self):
        """ Carga los registros en memoria """
        self.registros = self.db.listar_todos()
        self.indice_actual = 0

    def cargar_registros_libros(self):
        """ Carga los registros en memoria """
        self.registros = self.db.listar_libros()
        self.indice_actual = 0

    def mostrar_registro(self):
        """ Muestra el registro actual en los campos de texto """
        if not self.registros:
            return
        
        registro_actual = self.registros[self.indice_actual]
       
        for columna, campo in self.campos.items():
            campo.delete(0, tk.END)
            campo.insert(0, registro_actual[columna])
            


    def siguiente_registro(self):
        """ Muestra el siguiente registro """
        if self.indice_actual < len(self.registros) - 1:
            self.indice_actual += 1
            self.mostrar_registro()

    def anterior_registro(self):
        """ Muestra el registro anterior """
        if self.indice_actual > 0:
            self.indice_actual -= 1
            self.mostrar_registro()

    def modificar_registro(self):
        """ Modifica el registro actual """
        if not self.registros:
            return

        id_registro = self.registros[self.indice_actual]["id"]
        nuevos_datos = {columna: campo.get()
                        for columna, campo in self.campos.items()}

        self.db.modificar_registro(id_registro, nuevos_datos)
        self.cargar_registros()
        self.mostrar_registro()
        messagebox.showinfo("Éxito", "Registro modificado correctamente.")

    def eliminar_registro(self):
        """ Elimina el registro actual """
        if not self.registros:
            return

        id_registro = self.registros[self.indice_actual]["id"]

        respuesta = messagebox.askyesno(
            "Confirmación", "¿Está seguro de eliminar este registro?")
        if respuesta:
            self.db.eliminar_registro(id_registro)
            self.cargar_registros()
            if self.registros:
                self.mostrar_registro()
            else:
                messagebox.showinfo("Información", "No hay más registros.")
                self.frame_gestion.pack_forget()

    def abrir_formulario_nuevo(self):
        """ Abre un formulario emergente para insertar un nuevo registro """
        ventana_nuevo = tk.Toplevel(self.root)
        ventana_nuevo.title("Nuevo Registro")
        ventana_nuevo.geometry("400x300")

        ttk.Label(ventana_nuevo, text="Ingrese los datos:").pack()

        campos_nuevo = {}

        # 🔹 Excluir el campo `id` de la entrada del usuario
        columnas_sin_id = [col for col in self.columnas if col.lower() != "id"]

        for columna in columnas_sin_id:
            ttk.Label(ventana_nuevo, text=columna).pack()
            campo = ttk.Entry(ventana_nuevo)
            campo.pack()
            campos_nuevo[columna] = campo

        def guardar_nuevo():
            """ Guarda el nuevo registro en la base de datos """
            nuevo_registro = {columna: campo.get()
                              for columna, campo in campos_nuevo.items()}

            # 🔹 Insertamos solo los campos sin `id`
            self.db.crear_registro(nuevo_registro)
            self.cargar_registros()
            self.mostrar_registro()
            ventana_nuevo.destroy()
            messagebox.showinfo("Éxito", "Registro agregado correctamente.")

        ttk.Button(ventana_nuevo, text="Guardar",
                   command=guardar_nuevo).pack(pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
