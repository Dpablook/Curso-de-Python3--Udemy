#Objetos en Python
#Todo es un objeto en python
#Que es un objeto? algo que tenga funciones y atributos como cualquier objeto de la vida real
#Un metodo de un objeto es cuando un funcion esta dentro de un objeto
#Se activa poniendo un punto

#Ejemplo de Objetos en funciones
#Se le agraga el objeto .upper() para que el elif aparesca en mayuscula
edad=15
edad_2=35

def bar(edad):
    if edad==20:
        print("Entrar")
    elif edad<20:
        print("Casi pero no".upper())
    else:
        print("No puedes entrar")

bar(edad)
bar(edad_2)