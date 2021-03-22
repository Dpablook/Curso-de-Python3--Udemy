#Las funciones estan presentes en  cualquier lenguaje
#las funciones permiten encapsular partes del codigo para no repetirlas una y otra vez
#Permite que el codigo sea mas mantenible

print("Mi nombre es Pablo")

#para definir nuestras propias funciones en Python se coloca:
def pedir_pizza():
    print("pedir pizza")

#Luego de defnir la podemos ejecutar
pedir_pizza()

#Tambien se les puede poner una condicion dentro de una funcion:

edad=15
edad_2=35

def bar(edad):
    if edad==20:
        print("Entrar")
    elif edad<20:
        print("Casi pero no")
    else:
        print("No puedes entrar")

bar(edad)
bar(edad_2)

#Las funciones se separan con_el_guion_bajo
#Tambien se pueden con Majusculas en las palabras que le siguen (palabrasQueSiguen)


