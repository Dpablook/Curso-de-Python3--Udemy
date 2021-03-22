#Calculadora
#Ejercicico para hacer una calculadora

def realizar_operacion(operacion, primero, segundo):
    if operacion == "1":
        return primero + segundo;
    elif operacion == "2":
        return primero - segundo;
    elif operacion == "3":
        return primero * segundo;
    else:
        return primero / segundo;

print("Bienvenido a la calculadora")
operacion = input("Por favor indetifique la operacion que desea realizar \n1.Suma\n2.restan\n3.multiplicacion \n4.division\nIngresar el numero correspondiente:")

primero = int(input("Ingrese el primer numero: "))
segundo = int(input("Ingrese el segundo numero"))

resultado = realizar_operacion(operacion, primero, segundo)

print(resultado)


continuar = input("Desea continuar? si/no")

if continuar == "no";
    continue

print("Gracias por usar mi calculadora, saludos.")

