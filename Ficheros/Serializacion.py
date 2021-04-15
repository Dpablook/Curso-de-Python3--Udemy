#Serializacion
#tranformar codigo en codigo binario

import pickle

# fichero = open("lista_nombres", "wb")
# lista= ["Maria", "Pedro", "Jose"]
# pickle.dump(lista,fichero)
# fichero.close()


#Para leer
#

fichero = open("lista_nombres", "rb") 
lista = pickle.load(fichero)
print(lista)#de esta forma ya se imprime la lista pasada de Binario


