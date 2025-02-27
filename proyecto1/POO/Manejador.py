from Database import Database

db=Database('localhost','root','root','app','roles')

roles=db.crear_registro({'nombre':'usuario','descripcion':'Usuario normal'})
print(roles)

