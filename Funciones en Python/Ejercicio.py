
#Ejercicio 1:
#(1) Escribir una función a la que se le pase una cadena <nombre> y muestre por pantalla el saludo ¡hola <nombre>!.

#def saludar(nombre):
#	print("Hola " + nombre)
#	return 

#saludar("Pablo")

#Ejercicio 2:
#(2) Solicitar al usuario que ingrese su dirección email. 
#Imprimir un mensaje indicando si la dirección es válida o no, valiéndose de una función para decidirlo.
#Una dirección se considerará válida si contiene el símbolo "@".

#def solicitud(email):
#	caracterBuscado = "@"
#	validar = False
#	for c in email:
#		if c == caracterBuscado:
#			return True
#	return False

#dirección = input("Ingrese si email: ")
#if solicitud(dirección):
#	print("Es valida")
#else:
#	print("No es valida")




#Ejercicio 3:
#Crea una funcion con argumentos interminables, luego itera con un bucle sobre los argumentos y agregale clave y valor
#

#def argumentos(*args):
#	for args in args:
#   		print(args)

#argumentos("Hola","como","estan","?")

#def argumentos(**kwargs):
#  	print(kwargs)

#argumentos(a= "Hola",b= "como",c= "estan",d= "?")


#Ejercicio 4:
#Crea una funcion que nos devuelva numeros pares.
#

#def pares(numero):
#	numb = 1
#	lista = []

#	while numb<numero:
#		lista.append(numb*2)
#		numb=numb+1

#	return lista

#print(pares(100))


