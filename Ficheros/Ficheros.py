#ficheros
#abrir y cerrar archivos txt
#con los archivos externos se guarda la informacion
#dos alternativas trabajar con base de datos o con archivos externos
#tiene pasos:
#creacion --> apertura --> creacion y cierre

#1º paso : importar la libreria IO

from io import open

# fichero = open("archivo.txt","w")#La creacion y apertura
# #se pasan dos parametros nombre de archivo y la escritura (w)

# texto = "Hola Mundo\nEstudios Python"
# fichero.write(texto)#La manipulacion
# fichero.close()#El cierre

# #De esta forma se crea el fichero con el contenido
# #
# #como se hace para leer???

# fichero = open("archivo.txt","r")
# texto = fichero.read()
# fichero.close()
# print(texto)

#Hay otro metodo que lee linea a linea y luego lo almacena en una lista

# fichero = open("archivo.txt","r")
# texto = fichero.readlines()
# fichero.close()
# print(texto)
# print(texto[0])#Se puede manipular de forma diferente

fichero = open("archivo.txt","a")
fichero.write("\n Esto es el metodo append")
fichero.close()
print(fichero)#Nos muestra el espacio en memoria
#Y lo agrega al contenido