#Diccionarios
# Son una coleccion de elementos que estan indexados no estan ordenados y se pueden modificar

diccionario_colores={"red":"rojo","blue":"azul","green":"verde"}
print(diccionario_colores)

#Si queremos acceder a un valor imprimimos su posicion
print(diccionario_colores["red"])

#Se pueden guardar en variables (obvio)
valor = diccionario_colores["blue"]
print(valor)

#Se pueden agragar valores
diccionario_colores["black"]="negro"
print(diccionario_colores)

#Tambien se pueden eliminar
diccionario_colores.pop("red")
print(diccionario_colores)

#Si queremos recorrerlo
for color in diccionario_colores:
    print(color)

#Para imprimir tanto la clave como el valor
for clave,valor in diccionario_colores.items():
    print(clave,valor)