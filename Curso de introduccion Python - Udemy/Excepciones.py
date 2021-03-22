#Excepciones

#Ejercicio para sacar una suma con el usuario

a = int(input("Numero1:"))
b = int(input("Numero2:"))

suma = a + b

print ("El resultado es: " + str(suma))

#En caso de que el usuario ponga numeros en letras por ejemplo

try:
    a = int(input("Numero1:"))
    b = int(input("Numero2:"))
except ValueError:
    print("Ese no es un numero")
else:
    suma = a + b
    print ("El resultado es: " + str(suma))
