from panel_Principal.form_maestro_design import FormMaestro
from config.install import check_and_install_pillow

if __name__ == "__main__":
    check_and_install_pillow()
    app = FormMaestro()
    app.mainloop()
