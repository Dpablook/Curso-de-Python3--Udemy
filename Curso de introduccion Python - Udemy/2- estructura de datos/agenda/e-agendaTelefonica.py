#AGENDA TELEFONICA

agenda_telefonica = dict()



def imprimir_operacion(nombre_operacion):
	print()
	print("-----------AGENDA TELEFONICA----------------")
	print(nombre_operacion)
	print("--------------------------------------------")
	print()

def agregar_contacto():
	nombre = input("Nombre del nuevo contacto:  ")
	numero = input("Nombre del nuevo contacto:  ")
	agenda_telefonica[nombre] = numero

	imprimir_operacion("Contacto Agregado")




def remover_contacto():
	nombre = input("Nombre del contacto que deseas borrar: ")
	nombre_operacion = None 
	
	try:
		del agenda_telefonica[nombre]
	except KeyError:
		nombre_operacion = "Ese contacto no existe"
	else:
		nombre_operacion = "Contacto borrado"

	imprimir_operacion(nombre_operacion)



def actualizar_contacto():
	nombre = input("Nombre del contacto que deseas actualizar: ")
	numero = input("Nuevo numero de este contacto: ")
	
	agenda_telefonica[nombre] = numero
	
	imprimir_operacion("Contacto Actualizado")



def ver_contacto():
	nombre = input("Nombre del contacto: ")
	nombre_operacion = None

	try:
		nombre_operacion = "{} - {}" .format(nombre,agenda_telefonica[nombre])
	except KeyError:
		nombre_operacion = "Ese contacto No existe "

	imprimir_operacion(nombre_operacion)




def ver_todos():
	nombre_operacion = None

	if len(agenda_telefonica) == 0:
		nombre_operacion = "No tienes ningun contacto"
	else:
		for contacto in agenda_telefonica:
			#print(contacto + " - " + agenda_telefonica[contacto])
			if nombre_operacion = None:
				nombre_operacion = "{} - {}" .format(contacto,agenda_telefonica[contacto])
			else: 
				nombre_operacion += "\n {} - {}" .format(contacto,agenda_telefonica[contacto])
	
	imprimir_operacion(nombre_operacion)

print("Bienvenido a la agenda Telefonica")

while True:
	print("1- Agregar Contacto")
	print("2- Remover Contacto")
	print("3- Actualizar Contacto")
	print("4- Ver Contacto")
	print("5- Ver todos los contactos")
	print("6- Salir")

	try:
		operacion = int(input(":  "))
	except ValueError:
		print("Selecciona un numero del 1 al 6 ")
	else:
		if operacion == 1:
			agregar_contacto()
		elif operacion == 2:
			remover_contacto()
		elif operacion == 3:
			actualizar_contacto()
		elif operacion == 4:
			ver_contacto()
		elif operacion == 5:
			ver_todos()
		elif operacion == 6:
			break
		else:
			print("Operacion Desconocida")

print()
print("Gracias por usar la agenda")
print()

