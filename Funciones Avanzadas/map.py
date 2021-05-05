#Toma una funcion y la aplica a cada elemento de una lista
#
#
#


def doblar(numero):
	return numero*2

numeros = [2,5,10,23,50,33]
i = map(doblar, numeros)#Aplica la funcion doblar a cada elemento de la lista numeros
print(list(i))

