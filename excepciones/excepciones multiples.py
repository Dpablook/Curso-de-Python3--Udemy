#Excepciones Multiples


#Con este codigo nos dice como se llama el error
try:
    c = int(input("Ingrese un valor: "))
    c/0

#Aqui podemos poner mas de una excepcion
#y aclararle al usuario el error:

except ValueError:
    print("No se puede ingresar un texto.")
except Exception as c:
    print(type(c).__name__)
