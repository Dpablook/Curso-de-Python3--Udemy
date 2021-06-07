# Doctest - generar pruebas dentro de la documentacion
# 
# 
def sumar(numero1, numero2):
	"""
	Esto es la documentacion de esta funcion
	recibe dos numeros como parametros y develve su suma

	
	>>> sumar(4,3)
	7
	>>> sumar(5,3)
	9
	>>> sumar(1,3)
	7
	"""

	return numero1 + numero2


resultado= sumar(2,4)
print(resultado)


import doctest
doctest.testmod()
