# Se le puede pasar todo tipo de argumentos sin limites 

def infinito(*args):
	print(args)

infinito("hola", 20, 55, "Saludos", [10,20,25,30])

#Se genera una tupla


#Se puden agragarle claves y valores de esta forma:
def infinito2(**kwargs):
	print(kwargs)

infinito2(a="Hola", b=2500, c=[10,20,30], d=["Maria", "Jose", "Esteban"])

#Para imprimirlo se hace de esta forma:

def infinito3(**kwargs):
	for kwarg in kwargs:
		print(kwarg, "----->", kwargs[kwarg])

infinito3(a="Hola", b=2500, c=[10,20,30], d=["Maria", "Jose", "Esteban"])