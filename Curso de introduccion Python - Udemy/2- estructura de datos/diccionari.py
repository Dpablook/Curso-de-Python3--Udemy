#Diccionarios
>>> lista_calificaciones = [9,10,6,5]
>>> lista_calificaciones
[9, 10, 6, 5]
>>> #Diccionarios
>>> diccionario_calif={"pablo":9,"Dario":10,"Juan":6,"Kevin":5}
>>> diccionario_calif
{'Dario': 10, 'Kevin': 5, 'Juan': 6, 'pablo': 9}
>>> #Ojo no siempre se respeta el orden
>>> diccionario_calif["Juan"]
6
>>> diccionario_calif[9]
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    diccionario_calif[9]
KeyError: 9
>>> diccionario_calif["Kevin"]="Esteban"
>>> diccionario_calif
{'Dario': 10, 'Kevin': 'Esteban', 'Juan': 6, 'pablo': 9}
>>> dict([["Pepe",7],["Maria",10]])
{'Pepe': 7, 'Maria': 10}

#Para agregar elmentos utilizamos
>>> dias_semana={"Lunes":9,"Martes":10,"Miercoles":11,"Jueves":12,"Viernes":13}
>>> dias_semana
{'Viernes': 13, 'Miercoles': 11, 'Jueves': 12, 'Martes': 10, 'Lunes': 9}
>>> dias_semana.update{("Sabado":14,"Domingo":15)}
SyntaxError: invalid syntax
>>> dias_semana.update({"Sabado":14,"Domingo":15})
>>> dias_semana
{'Viernes': 13, 'Miercoles': 11, 'Jueves': 12, 'Lunes': 9, 'Domingo': 15, 'Sabado': 14, 'Martes': 10}

#iteracion

>>> calif={"Pablo":9,"Kevin":6,"Pedro":8}
>>> calif
{'Pedro': 8, 'Kevin': 6, 'Pablo': 9}

>>> for calificacion in calif:
	print(calificacion)

	
Pedro
Kevin
Pablo
>>> for calificacion in calif:
	print(calif[calificacion])

	
8
6
9

>>> for key in calif.keys():
	print(key)

	
Pedro
Kevin
Pablo
>>>
>>> for value in calif.values():
	print(value)

	
8
6
9
>>> for item in calif.items():
	print(item)

	
('Pedro', 8)
('Kevin', 6)
('Pablo', 9)
>>>