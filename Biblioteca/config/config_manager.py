import configparser

class ConfigManager:
    def __init__(self, config_file='config.ini'):
        self.config = configparser.ConfigParser()
        self.config.read(config_file)

    def get_database_config(self):
        try:
            return {
                'host': self.config.get('database', 'host'),
                'user': self.config.get('database', 'user'),
                'password': self.config.get('database', 'password'),
                'database': self.config.get('database', 'database'),
                # 'use_pure': self.config.getboolean('database', 'use_pure')
            }
        except configparser.NoSectionError:
            print(
                "Error: La sección 'database' no existe en el archivo de configuración.")
            return None
        except configparser.NoOptionError as e:
            print(f"Error: Falta la opción {e} en la sección 'database'.")
            return None

    def set_database(self, new_database):
        if not self.config.has_section('database'):
            self.config.add_section('database')

        self.config.set('database', 'database', new_database)
        with open('config.ini', 'w', encoding='utf-8') as configfile:
            self.config.write(configfile)
            print(f"Base de Datos cambiada a {new_database}")
