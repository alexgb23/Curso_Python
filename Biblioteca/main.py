from panel_Principal.form_maestro_design import FormMaestro

from config.install_dependency import check_and_install_pillow, check_and_install_mysql

if __name__ == "__main__":
    check_and_install_pillow()
    check_and_install_mysql()
    app = FormMaestro()
    ## Ocultar la barra de título y los botones
    # app.winfo_toplevel().overrideredirect(True)

    # # Hacer que la ventana esté siempre en la parte superior
    # app.attributes("-topmost", True)  # Mantiene la ventana por encima de otras
    # app.lift()  # Lleva la ventana al frente
    # app.focus_force()  # Fuerza el foco en la ventana
    app.mainloop()

