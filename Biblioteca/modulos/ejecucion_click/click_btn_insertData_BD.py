from tkinter import messagebox
from clases.libros import Libros
from clases.editoriales import Editoriales
from clases.autores import Autores
import modulos.ejecucion_click.click_btn_menu_lateral as click_btn_menu_lateral


def acciones_botones_sub_panel(self, tabla, boton):
    if boton['text'] == "Actualizar":
        actualizar(self, tabla)
    elif boton['text'] == "Insertar":
        insertar(self, tabla)


def obtener_datos_editorial(cadena_busqueda):
    edit = Editoriales()
    campos_a_buscar = ['nombre']  # Reemplaza con los campos reales de tu tabla
    resul = edit.filtrar(campos_a_buscar, cadena_busqueda)
    return resul[0]['id'] if resul else None



def mostrar_mensaje(resultado, entidad, accion):
    if resultado is not None:
        messagebox.showinfo("Informacion", f"{entidad} {'actualizado' if accion == 'update' else 'creado'} correctamente" + (f" con id: {resultado}" if accion == 'insert' else ""))
    else:
        messagebox.showerror("Error", f"Error al {'actualizar' if accion == 'update' else 'crear'} el {entidad}")

def actualizar(self, tabla):
    nuevos_datos = {}
    id = self.campos_actualizar["id"].get()
    
    if tabla == "Libros":
        nuevos_datos['titulo'] = self.campos_actualizar["titulo"].get()
        nuevos_datos['anio'] = self.campos_actualizar["anio"].get()
        cadena_busqueda = self.campos_actualizar["editorial"].get()
        nuevos_datos['id_editorial'] = obtener_datos_editorial(cadena_busqueda)
        resultado = Libros().modificar_registro(id, nuevos_datos)
        mostrar_mensaje(resultado, "Libro", "update")
        click_btn_menu_lateral.instanciar(self, "Libros")
        
    elif tabla == "Autores":
        nuevos_datos['nombre'] = self.campos_actualizar["nombre"].get()
        nuevos_datos['apellido'] = self.campos_actualizar["apellido"].get()
        nuevos_datos['nacionalidad'] = self.campos_actualizar["nacionalidad"].get()
        resultado = Autores().modificar_registro(id, nuevos_datos)
        mostrar_mensaje(resultado, "Autor", "update")
        click_btn_menu_lateral.instanciar(self, "Autores")
        
    elif tabla == "Editoriales":
        nuevos_datos['nombre'] = self.campos_actualizar["nombre"].get()
        nuevos_datos['direccion'] = self.campos_actualizar["direccion"].get()
        nuevos_datos['telefono'] = self.campos_actualizar["telefono"].get()
        resultado = Editoriales().modificar_registro(id, nuevos_datos)
        mostrar_mensaje(resultado, "Editorial", "update")
        click_btn_menu_lateral.instanciar(self, "Editoriales")
        
    elif tabla == "Autor-Libro":
        # Lógica para Autor-Libro si es necesario
        pass

def insertar(self, tabla):
    nuevos_datos = {}
    
    if tabla == "Libros":
        nuevos_datos['titulo'] = self.campos_insertar["titulo"].get()
        nuevos_datos['anio'] = self.campos_insertar["año"].get()
        cadena_busqueda = self.campos_insertar["editorial"].get()
        nuevos_datos['id_editorial'] = obtener_datos_editorial(cadena_busqueda)
        resultado = Libros().crear_registro(nuevos_datos)
        mostrar_mensaje(resultado, "Libro", "insert")
        click_btn_menu_lateral.instanciar(self, "Libros")
        
    elif tabla == "Autores":
        nuevos_datos['nombre'] = self.campos_insertar["nombre"].get()
        nuevos_datos['apellido'] = self.campos_insertar["apellido"].get()
        nuevos_datos['nacionalidad'] = self.campos_insertar["nacionalidad"].get()
        resultado = Autores().crear_registro(nuevos_datos)
        mostrar_mensaje(resultado, "Autor", "insert")
        click_btn_menu_lateral.instanciar(self, "Autores")
        
    elif tabla == "Editoriales":
        nuevos_datos['nombre'] = self.campos_insertar["nombre"].get()
        nuevos_datos['direccion'] = self.campos_insertar["direccion"].get()
        nuevos_datos['telefono'] = self.campos_insertar["telefono"].get()
        resultado = Editoriales().crear_registro(nuevos_datos)
        mostrar_mensaje(resultado, "Editorial", "insert")
        click_btn_menu_lateral.instanciar(self, "Editoriales")

        
    elif tabla == "Autor-Libro":
        # Lógica para Autor-Libro si es necesario
        pass
