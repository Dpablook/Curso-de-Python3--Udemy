#Funcion Filter se usa para crear un nuevo iterador (lista o diccionario)
#Nos ayuda a filtrar en un lista


edades = [10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100]

def mayores(edad):
	return edad>=21


entrar = list(filter(mayores, edades))

print(entrar)