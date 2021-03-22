#Reloj del mundo

#Hora new york, san francisco, los angeles

import datetime

print ("Bienvenido al reloj del mundo")
print("Estas son las operaciones que puedes realizar: ")
print("1 ver la hora")
print("2 ver la fecha y hora")
print("3 ver la hora en Nueva York")
print("4 ver la hora en San Francisco")
print("5 ver las instrucciones nuevamente")
print("6 Salir")

while True:
    operacion = input(": ")

    if operacion == "1":
        print(datetime.datetime.now().time())
    elif operacion == "2":
        print(datetime.datetime.now())
    elif operacion == "3":
        print("La hora en Nueva York")
    elif operacion == "4":
        print("La hora en San Francisco")
    elif operacion == "5":
        print("Ver instrucciones")
    elif operacion == "6":
        break
    else:
        print("No reconozco esa operacion")