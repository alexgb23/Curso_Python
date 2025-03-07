from clases.baseorm import BaseORM

class Editoriales(BaseORM):
    tabla = "editoriales"
    
    def __init__(self):
        super().__init__()
        self.editoriales = super().listar_todos()  


    def listar_editoriales(self):
        for editorial in self.editoriales:
            id = editorial.get('id')  
            nombre = editorial.get('nombre')  
            direccion= editorial.get('direccion')
            telefono = editorial.get('telefono')
            print(f'ID: {id}, Nombre: {nombre}, Direccion: {direccion}, Telefono: {telefono}')  

