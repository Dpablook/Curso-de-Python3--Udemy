# Como generar un uni test con python
# 
# el unitest es una prueba dentro del codigo de python
# 


def multiplicar(numero1, numero2):
	return numero1 * numero2

resultado = multiplicar(2,4)
print(resultado)


import unittest

class pruebas(unittest.TestCase):

	def test(self):
		self.assertEqual(multiplicar(2,4),8)
		self.assertEqual(multiplicar(2,4),9)

if __name__ == '__main__':
	unittest.main()

# dio resultado fail por supuesto pero esta bien