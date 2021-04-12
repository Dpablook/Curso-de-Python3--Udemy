#Que es el polimorfismo???
#El concepto de polimorfismo (del griego muchas formas) implica que si en una porción de código 
#se invoca un determinado método de un objeto, podrán obtenerse distintos resultados según la clase del objeto.
#
#

#Cual metodo va a llamar?
class Persona:
	def __init__(self):
		self.cedula=1234
	def mensaje(self):
		print("Este mensaje viene de la clase persona")

class Obrero(Persona):
	def __init__(self):
		self.especialista=1
	def mensaje(self):
		print("Este mensaje viene de la clase obrero")

obrero_planta=Obrero()
obrero_planta.mensaje()#Llama al de la clase obrero
#Llama al de la clase que se hace referencia