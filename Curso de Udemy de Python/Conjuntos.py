#Conjuntos
# son coleccion de elementos pero que estan desordenados

conjunto_colores = {"azul", "rojo","verde"}
print(conjunto_colores)

#Pero no podemos acceder a alguna de sus posiciones
#ERROR
#print(conjunto_colores[0])

#Si queremos agregar elementos los va a agregar en cualquier lugar

conjunto_colores.add("negro")
print(conjunto_colores)

conjunto_colores.add("blanco")
print(conjunto_colores)

#Tambien se pueden borrar elementos de forma normal