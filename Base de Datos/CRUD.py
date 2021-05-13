import sqlite3

conexion = sqlite3.connect("Productos.db")


cursor=conexion.cursor()

#leer
# cursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION_P='Panaderia'")#panaderia no debe ir en mayusculas
# productos = cursor.fetchall()
# print(productos)

#actualizar
# cursor.execute("UPDATE PRODUCTOS SET SECCION_P='PANADERIA' WHERE SECCION_P='Panaderia'")
# Esto actualiza la base de datos en la palabra Panaderia

# Eliminar
# ojo con no eliminar todo aplicando el where

# cursor.execute("DELETE FROM PRODUCTOS WHERE ID = AR2")
# aca salio el error por que no esta actualizada la base de datos en la columna id=2 de la parte anterior


# y listo con esto tenemos un CRUD seguir practicando

conexion.commit()
conexion.close()