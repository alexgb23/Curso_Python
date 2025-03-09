
from clases.libros import Libros
from clases.editoriales import Editoriales
from clases.autores import Autores
from clases.autorlibro import AutorLibro
import modulos.botones.btn_selected as btn_selected
from tkinter import messagebox
import modulos.efectos_visuales.transisiones as transition
import modulos.ejecucion_click.click_btn_menu_lateral as click_btn_menu_lateral
import modulos.paneles.tabla as tabla

def acciones(self, buton, btn_info_sup):
    btn_selected.marcar_boton(self, buton, btn_info_sup, True)

    # Manejo de acciones según el texto del botón
    accion_texto = btn_info_sup["text"]


    if self.titulo_panel_administracion == "Bienvenido a eDe-Lib":
        messagebox.showinfo("Error", f"Debe seleccionar en el menu lateral que desea {accion_texto}")
        return

    # Verificar si hay una fila seleccionada antes de procesar otras acciones
    if accion_texto in ["Actualizar", "Eliminar"] and not self.campo_selected_table:
        tabla.actualizar_tabla(self, self.registros)
        messagebox.showinfo("Error", "Seleccione una fila en la tabla para actualizar")
        return
        
    if accion_texto == "Eliminar":
        # Mensaje de confirmación basado en el título del panel
        if self.titulo_panel_administracion == "Libros":
            mensaje = f"¿Está seguro de que desea eliminar el libro '{self.campo_selected_table.get('titulo', 'desconocido')}'?"
        elif self.titulo_panel_administracion == "Editoriales":
            mensaje = f"¿Está seguro de que desea eliminar la editorial '{self.campo_selected_table.get('nombre', 'desconocido')}'?"
        elif self.titulo_panel_administracion == "Autores":
            nombre_autor = self.campo_selected_table.get('nombre', 'desconocido')
            apellido_autor = self.campo_selected_table.get('apellido', 'desconocido')
            mensaje = f"¿Está seguro de que desea eliminar el autor '{nombre_autor} {apellido_autor}'?"
        else:
            mensaje = "¿Está seguro de que desea eliminar el registro seleccionado?"

        respuesta = messagebox.askyesno("Confirmar Eliminación", mensaje)
        if respuesta:  # Si el usuario acepta
            eliminar_registro(self)
        return

    self.transicion_paneles_if_true()
    self.creacion_acciones_cuerpo_datos(accion_texto)
    transition.slide_in(self, self.panel_acciones_cuerpo)

 

def eliminar_registro(self):
    model_mapping = {
        "Libros": Libros,
        "Editoriales": Editoriales,
        "Autores": Autores,
        "AutorLibro": AutorLibro
    }

    modelo = model_mapping.get(self.titulo_panel_administracion, AutorLibro)
    respuesta = modelo().eliminar_registro(self.campo_selected_table["id"])
    
    if respuesta is not None:
        messagebox.showinfo("Informacion", f"{self.titulo_panel_administracion} eliminado correctamente")
    else:
        messagebox.showerror("Error", f"Error al eliminar el {self.titulo_panel_administracion.lower()}")

    click_btn_menu_lateral.instanciar(self, self.titulo_panel_administracion)
