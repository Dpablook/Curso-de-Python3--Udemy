#Como leer Archivos

import re
archivo = open("sample.txt",encoding="utf-8")

informacion = archivo.read()

archivo.close()

print(informacion)

#imprime lo que tiene el archivo de texto sample.txt :)