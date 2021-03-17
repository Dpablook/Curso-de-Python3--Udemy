#En Python es con
# IF
# ELIF
# ELSE

a = 20
b = 20
c = 15

if (a > b):
	print("a es mayor a b")
elif (a == b):
	print("Son iguales")
else:
	print("a es menor a b")

#No tiene mucha complicacion
# Con doble condicion se pone and o or

if (a == b) and (a > c):
	print("si se cumple AND")
else:
	print("No se cumple")

if (a == b) or (a == c):
	print("si se cumple AND")
else:
	print("No se cumple")