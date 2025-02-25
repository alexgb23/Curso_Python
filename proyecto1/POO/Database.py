class Database:
    host = 'localhost'
    user = 'root'
    password = 'root'
    db = 'app'
    
    def __init__(self):
        self.connection = None

    def connect(self):
        self.connection = f"Conexión a {self.host} exitosa"