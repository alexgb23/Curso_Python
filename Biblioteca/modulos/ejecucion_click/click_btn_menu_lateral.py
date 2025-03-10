import modulos.botones.btn_selected as btn_selected
import modulos.paneles.crear_panel_admin as crear_panel_admin
from clases.libros import Libros
from clases.editoriales import Editoriales
from clases.autores import Autores
from clases.autorlibro import AutorLibro
import modulos.paneles.crear_tabla_bd as crear_tabla



#metodo para asocial diferentes metodos llamado al hacer clic en cualquier boton del menu lateral
def instanciar_y_marcar(self, boton, btn_info):
    # Llama a los métodos deseados
    btn_selected.marcar_boton(self, boton, btn_info)  # Marca el botón
    instanciar(self, btn_info["text"])   # Llama a instanciar

#metodo el cual instancia la clase dependiendo del nombre del boton y carga los datos en el panel 
def instanciar(self, clase):
    btn_selected.reset_btn_sup(self)
    self.campo_selected_table = {}
    clases_mapping = {
        "Libros": (Libros, "libros_con_autor_y_editorial"),
        "Autores": (Autores, "autores"),
        "Editoriales": (Editoriales, "editoriales"),
        "Autor-Libro": (AutorLibro, "autor_libros")
    }

    if clase in clases_mapping:
        try:
            self.registros = None
            clase_obj, atributo = clases_mapping[clase]
            instancia = clase_obj()
            self.registros = getattr(instancia, atributo)
            self.indice_actual = 0
            self.titulo_panel_administracion = clase
            crear_panel_admin.cargarDatos(self)
        except Exception as e:
            print(f"Error al instanciar {clase.lower()}: {e}")
    elif clase == "Inicio":
        crear_panel_admin.cargarDatos(self, "Inicio")
    else:
        crear_tabla.nueva_tabla_Base_Datos(self)

