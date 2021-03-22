#Ciclos
#importacia de no hacer tareas repetitivas
#un ciclo nos ayuda a repetir un proceso una y otra vez
#los ciclos for y wihile
#Los ciclos wihile no ayuda a repetir un codigo siempre que una condicion sea cierta
#Los ciclos for nos ayuda a recorrer los elementos en una coleccion de cosas

manzanas = 10

#while manzanas > 0:
#    print("me estoy comiendo una manzana")
    #manzanas = manzanas - 1
#    manzanas -= 1

#se repite 10 veces

#para ponerle numero a cada elemento se usa esto
while manzanas > 0:
    print("me estoy comiendo la manzana #" + str(manzanas))
    #manzanas = manzanas - 1
    manzanas -= 1

print("me quede sin manzanas")

#Los ciclos for
#Se usa para imprimir todos los numeros

lista_numero = [1,2,3,4,5,6,8,9,10]

for numero in lista_numero:
    print(numero)

#para dar un corte
#con el uso de break, lo que hace es romper el ciclo

for numero in lista_numero:
    if numero >5:
        break
    print(numero)

#con continue se saltea una interaccion del ciclo
#no se imprime el numero 5 por ejemplo
for numero in lista_numero:
    if numero ==5:
        continue
    print(numero)

