from panel_Principal.form_maestro_design import FormMaestro
from config.install_dependency import *

if __name__ == "__main__":
    check_and_install_pillow()
    check_and_install_mysql()
    app = FormMaestro()
    app.mainloop()
