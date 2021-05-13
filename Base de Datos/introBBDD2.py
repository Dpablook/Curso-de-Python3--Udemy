import sqlite3

conexion = sqlite3.connect("Productos.db")


# claves primarias
# 
# 


cursor=conexion.cursor()

cursor.execute('''
	CREATE TABLE PRODUCTOS(
		CODIGO_P VARCHAR(10)PRIMARY KEY, #ESTO NO SE PUEDE REPETIR SINO NOS DA ERROR
		NOMBRE_P VARCHAR(10),
		SECCION_P VARCHAR(10))

''')

productos = [
	('AR1', 'Leche', 'Lacteos'),
	('AR2', 'Facturas', 'Panaderia'),
	('AR3', 'Asado', 'Caniceria'),
]


cursor.executemany("INSERT INTO PRODUCTOS VALUES(?,?,?)", productos)

# si volvemos a poner un articulo como por ejemplo AR3 nos va a tirar error 
# por las llaves que pusimos antes
# tira el error de tipo UNIQUE
# 
# 
# esto se puede solucionar con un auto incrementado
# 
# 
# ID INTEGER PRIMARY KEY AUTOINCREMENT (al principio de la creacion de la tabla)
# esto lo hace automaticamente
# evita que uno ponga AR1 , AR2 y AR3
# y en ves de (?,?,?) => (null,?,?)
# 
# 
# 
# 
# 

conexion.commit()
conexion.close()