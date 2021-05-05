#Los Generadores
#Son estructuras que se almancenan que estructura iterables
#
#

# Este es el metodo tradicional
def generapares(limite):
	num=1
	milista=[]
	while num<limite:
		milista.append(num*2)
		num=num+1
	return milista
print(generapares(10))


#Con los Generadores (yield)
#si no queremos toda la lista hacemos lo siguiete:

def generapares2(limite):
	num=1
	milista=[]
	while num<limite:
		yield num*2
		num=num+1

devuelvePares=generapares2(10)
print(next(devuelvePares))
print("Otra linea")
print(next(devuelvePares))

# EL yield from
# 

#como ingresar a los subelementos de los elementos:
#

def devuelvePaises(*Paises):
	for elemento in Paises:
		yield from elemento

paises_devuelta = devuelvePaises("Argentina", "Brasil","Peru", "Chile")
print(next(paises_devuelta))
print(next(paises_devuelta))
print(next(paises_devuelta))
print(next(paises_devuelta))
