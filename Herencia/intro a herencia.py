#Que es la herencia?
#se trata de heredar caracteristicas de otras clases
#tiene su jerarquia para heredar(padres, hijos, etc)
#Tenemos la clase padre --> luego la subclase --> y luego superclase

class Persona(object):
	def __init__(self, nombre,edad, apellido, sexo):
		self.nombre=nombre
		self.edad=edad
		self.apellido=apellido
		self.sexo=sexo

	def datosPersonales(self):
		print("El Nombre de la persona es", self.nombre)
		print("La edad de la persona es", self.edad)
		print("El apellido de la persona es", self.apellido)
		print("El sexo de la persona es", self.sexo)

miPersona=Persona("Pablo",29,"Ramirez","Indefinido")
miPersona.datosPersonales()

print("*************\n")
#como se hace para heredar a otera clase
#poniendo en la nueva clase el parametro del objeto que queremos hacer heredar:

class Empleado(Persona):
	#Aqui tambien podemos crear nuestros propios metodos:
	def datosTrabajo(self,vacaciones, salario):
		print("Las vacaciones de la persona es", vacaciones) #aqui ya no es necesario poner el self. por que no estamos haciendo referencia a la clase padre
		print("El salario de la persona es", salario)

miPersona2=Empleado("Maria",20,"Ramirez","Femenino") #aqui debemos poner la clase subclase (Empleado)
miPersona2.datosPersonales()
miPersona2.datosTrabajo("en Noruega", "$20.000 dolares") #y luego darle los valores de las parametros

##Importante nunca una clase padre puede heredar de una clase subclase


#Que es la herencia multiple?
# Una clase hereda de otras clases
#

class clase1:
	def metodo1(self):
		print("Hola soy el metodo de la clase 1")

class clase2:
	def metodo2(self):
		print("Hola soy el metodo de la clase 2")

#La clase 3 hereda de las clases 1 y 2
class clase3(clase1,clase2):
	def metodo3(self):
		print("Hola soy el metodo de la clase 3")	


c = clase3()
c.metodo3()
c.metodo2()
c.metodo1()