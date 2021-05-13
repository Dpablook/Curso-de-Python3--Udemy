#En este momento nececitaria saber mas sql :(
#
#Los pasos para manejar base de datos son:
#
#Abrir y crear 
#crear un puntero
#Ejecutar consultas SQL
#Manejar consulta SQL
#Manejar consulta, insertar, leer, actualizar y borrar(CRUD)



import sqlite3

conexion = sqlite3.connect("PrimerBase.db")#establecemos conexion

# conexion.close()

# crear una tabla
# 
# para esto debemos crear un cursor
# 

cursor = conexion.cursor()
# cursor.execute("CREATE TABLE USUARIOS(NOMBRE VARCHAR(50), EDAD INTEGER, SEXO VARCHAR(50))")


# cursor.execute("INSERT INTO USUARIOS VALUES('Brian', 25,'Masculino')")#esto nos crea una tabla en la pestaña hoja de datos


# cursor.execute("SELECT * FROM USUARIOS")
# usuario = cursor.fetchone()
# print(usuario)#Esto nos imprime en la consola los datos de la base de datos
# print(usuario[0])
# print(usuario[1])

#Como insertar registros multiples

# creamos una variable

# usuarios = [
# 	('Brian', 25, 'Masculino'),
# 	('Ana', 65, 'Femenino'),
# 	('Jose', 35, 'Masculino')
# ]
# cursor.executemany("INSERT INTO USUARIOS VALUES(?,?,?)", usuarios) #Si vamos a base de datos y hoja de datos y actualizamos aparecen nuestra tupla


#como recuperamos la tabla?

cursor.execute("SELECT * FROM USUARIOS")
usuarios = cursor.fetchall()
print(usuarios)
for i in usuarios:
	print(i)



conexion.commit()
conexion.close()





conexion.close() 

