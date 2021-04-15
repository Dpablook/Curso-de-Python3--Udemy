#Punteros
#
#

from io import open

# fichero = open("Archivo2.txt", "w")
# texto ="Hola estamos trabajando con python viendo cursores"
# fichero.write(texto)
# fichero.close()

#Pero como se modifica el curso (la parte que titila)

# fichero = open("Archivo2.txt", "r")
# fichero.seek(5)#Desde la posicion 5 (se cuenta los espacios en blanco)
# print(fichero.read())#Ejecuta solo desde la posicion 5 en adelante
# fichero.close()

#como se situa el puntero?

fichero = open("Archivo2.txt", "r")
fichero.seek(len(fichero.read())/2)#se divide en la mitad
print(fichero.read())
fichero.close()


