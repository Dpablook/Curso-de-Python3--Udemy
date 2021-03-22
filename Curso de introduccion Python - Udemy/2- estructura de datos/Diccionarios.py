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