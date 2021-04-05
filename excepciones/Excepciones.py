#Errores

def suma(num1, num2):
	return num1+num2

def resta(num1, num2):
	return num1-num2

def multiplicar(num1, num2):
	return num1*num2

#Aca usamos un try y un except para reparar un error
#No olvidar el nombre del error

def dividir(num1, num2):
	try:
		return num1/num2
	except ZeroDivisionError:
		print("No se puede hacer la division")
		return "operacion no valida"
	

op1 = int(input("Introduce un numero: "))
op2 = int(input("Introduce un segundo numero: "))

operacion = (input("Introduce una opcion: "))

if operacion == "suma":
	print(suma(op1,op2))
elif operacion == "resta":
	print(resta(op1,op2))
elif operacion == "multiplicar":
	print(multiplicar(op1,op2))
elif operacion == "dividir":
	print(dividir(op1,op2))
else:
	print("ERROR ALGO SALIO MAL	")

print("EJECUTANDO...")

#Lo siguiente es generar un error en la division


