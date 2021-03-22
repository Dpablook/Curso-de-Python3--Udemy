lista_articulos = list()

def agregar_articulos():
	print("Agregar Articulos")

def remover_articulos():
	print("Agregar Articulos")

def ver_articulos():
	print("Agregar Articulos")

def no_ver_nada():
	print("No ver nada")


while True:
    print("Estas son las operaciones que puedes realizar")
    print("1- Agregar Articulos")
    print("2- Remover los articulos")
    print("3- Ver los Articulos")
    print("4- No ver nada")
    print("5- Salir")

operacion = int(input(":  "))

if operacion == 1:
	agregar_articulos()
elif operacion == 2:
	remover_articulos()
elif operacion == 3:
	ver_articulos()
elif operacion == 4:
	no_ver_nada()
elif operacion == 5:
	

print()
print("Gracias por usar nuestra lista de compras")
print("Vuelve pronto")