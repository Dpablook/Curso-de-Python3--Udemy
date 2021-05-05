#Una funcion Lambda es una funcion anonima
#se puede ejecutar sin nombre
#sirve para funciones mas simples
#

# Forma Traficional
def suma(x,y):
	return(x+y)

print(suma(2,5))

# Forma con Lambda

i = lambda x,y: x+y
print(i(5,10))

revertir = lambda cadena: cadena[::-1]
print(revertir("Python"))


