
from clases.libros import Libros
from clases.editoriales import Editoriales
from clases.autores import Autores
import modulos.botones.btn_selected as btn_selected
from tkinter import messagebox
import modulos.efectos_visuales.transisiones as transition
import modulos.ejecucion_click.click_btn_menu_lateral as click_btn_menu_lateral


  
def acciones(self, buton, btn_info_sup):
    btn_selected.marcar_boton(self, buton, btn_info_sup, True)

    # Manejo de acciones según el texto del botón
    accion_texto = btn_info_sup["text"]

    if accion_texto == "Buscar": 
        if self.titulo_panel_administracion == "Bienvenido a eDe-Lib":  
            messagebox.showinfo(
                "Error", "Debe seleccionar en el menu lateral que desea Buscar"
            )
            return
        self.transicion_paneles_if_true() 
        self.creacion_acciones_cuerpo_datos("Buscar")
        transition.slide_in(self, self.panel_acciones_cuerpo)
    elif accion_texto == "Actualizar":
        if self.titulo_panel_administracion == "Bienvenido a eDe-Lib":  
            messagebox.showinfo(
                "Error", "Debe seleccionar en el menu lateral que desea Insertar"
            )
            return
        # Verificar si hay una fila seleccionada antes de procesar otras acciones
        if not self.campo_selected_table:
            messagebox.showinfo(
            "Error", "Seleccione una fila en la tabla para actualizar")
            return  # Salir de la función si no hay selección
        self.transicion_paneles_if_true() 
        self.creacion_acciones_cuerpo_datos("Actualizar")
        transition.slide_in(self, self.panel_acciones_cuerpo)
    elif accion_texto == "Insertar":
        if self.titulo_panel_administracion == "Bienvenido a eDe-Lib": 
            messagebox.showinfo(
            "Error", "Debe seleccionar en el menu lateral que desea Insertar"
            )
            return
        self.transicion_paneles_if_true()      
        self.creacion_acciones_cuerpo_datos("Insertar")
        transition.slide_in(self, self.panel_acciones_cuerpo)
    elif accion_texto == "Eliminar":
        if self.titulo_panel_administracion == "Bienvenido a eDe-Lib": 
            messagebox.showinfo(
                "Error", "Debe seleccionar en el menu lateral que desea Insertar"
            )
            return
        # Verificar si hay una fila seleccionada antes de procesar otras acciones
        if not self.campo_selected_table:
            messagebox.showinfo(
            "Error", "Seleccione una fila en la tabla para actualizar")
            return  # Salir de la función si no hay selección
        eliminar_registro(self)
       
        

def eliminar_registro(self):
    if self.titulo_panel_administracion == "Libros":
        libro_eliminado = Libros()
        respuesta= libro_eliminado.eliminar_registro(self.campo_selected_table["id"])
        if respuesta is not None:
            messagebox.showinfo("Informacion","Libro eliminado correctamente")
        else:
            messagebox.showerror("Error","Error al eliminar el libro")
        click_btn_menu_lateral.instanciar(self, "Libros")

    elif self.titulo_panel_administracion == "Editoriales":
        editorial_eliminada = Editoriales()
        espuesta= editorial_eliminada.eliminar_registro(self.campo_selected_table["id"])
        if espuesta is not None:
            messagebox.showinfo("Informacion","Editorial eliminada correctamente")
        else:
            messagebox.showerror("Error","Error al eliminar la editorial")
        click_btn_menu_lateral.instanciar(self, "Editoriales")

    elif self.titulo_panel_administracion == "Autores":
        autor_eliminado = Autores()
        respuesta= autor_eliminado.eliminar_registro(self.campo_selected_table["id"])
        if respuesta is not None:
            messagebox.showinfo("Informacion","Autor eliminado correctamente")
        else:
            messagebox.showerror("Error","Error al eliminar el autor")
        click_btn_menu_lateral.instanciar(self, "Autores")
    else:
        AutorLibro = AutorLibro()
        respuesta= AutorLibro.eliminar_registro(self.campo_selected_table["id"])
        if respuesta is not None:
            messagebox.showinfo("Informacion","AutorLibro eliminado correctamente")
        else:
            messagebox.showerror("Error","Error al eliminar el AutorLibro")
        click_btn_menu_lateral.instanciar(self, "AutorLibro")
        
