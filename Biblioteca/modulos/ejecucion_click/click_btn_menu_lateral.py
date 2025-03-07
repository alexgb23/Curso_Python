import modulos.botones.btn_selected as btn_selected
import modulos.paneles.crear_panel_admin as crear_panel_admin
from clases.libros import Libros
from clases.editoriales import Editoriales
from clases.autores import Autores
from clases.autorlibro import AutorLibro



#metodo para asocial diferentes metodos llamado al hacer clic en cualquier boton del menu lateral
def instanciar_y_marcar(self, boton, btn_info):
    # Llama a los métodos deseados
    btn_selected.marcar_boton(self, boton, btn_info)  # Marca el botón
    instanciar(self, btn_info["text"])   # Llama a instanciar


#metodo el cual instancia la clase dependiendo del nombre del boton y carga los datos en el panel 
def instanciar(self, clase):
    btn_selected.reset_btn_sup(self)
    self.campo_selected_table = {}
    if clase == "Libros":
        try:
            self.registros = None
            libros = Libros()
            self.registros = libros.libros_con_autor_y_editorial
            self.indice_actual = 0
            self.titulo_panel_administracion = "Libros"
            crear_panel_admin.cargarDatos(self)
        except Exception as e:
            print(f"Error al instanciar libros: {e}")
    elif clase == "Autores":
        try:
            self.registros = None
            autores = Autores()
            self.registros = autores.autores
            self.indice_actual = 0
            self.titulo_panel_administracion = "Autores"
            crear_panel_admin.cargarDatos(self)
        except Exception as e:
            print(f"Error al instanciar autores: {e}")
    elif clase == "Editoriales":
        try:
            self.registros = None
            editoriales = Editoriales()
            self.registros = editoriales.editoriales
            self.indice_actual = 0
            self.titulo_panel_administracion = "Editoriales"
            crear_panel_admin.cargarDatos(self)
        except Exception as e:
            print(f"Error al instanciar editoriales: {e}")
    elif clase == "Autor-Libro":
        try:
            self.registros = None
            autorlibro = AutorLibro()
            self.registros = autorlibro.autor_libros
            self.indice_actual = 0
            self.titulo_panel_administracion = "Autor-Libro"
            crear_panel_admin.cargarDatos(self)
        except Exception as e:
            print(f"Error al instanciar autorlibro: {e}")

    elif clase == "Inicio":
        crear_panel_admin.cargarDatos(self,"Inicio")
    else:
        print("No se encontró la clase")
