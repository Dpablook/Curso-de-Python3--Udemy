#Match y Search

import re
archivo = open("sample.txt",encoding="utf-8")
informacion = archivo.read()
archivo.close()

#Match es para buscar en el archivo sample caracteres que pueda contener
print(re.match(r"abcdefghijklmnopqrstuvwxyz",informacion))

#Si falta alguno por ejemplo a letra a , tira error (none)
print(re.match(r"bcdefghijklmnopqrstuvwxyz",informacion))

#match solo busca en una sola linea de codigo
#A diferencia de search busca en todas las lineas
print(re.search(r"0123456789",informacion))



