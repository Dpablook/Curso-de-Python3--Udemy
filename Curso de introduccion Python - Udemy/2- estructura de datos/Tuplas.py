#Tuplas

>>> #Se parecen en las listas pero son elementos estaticos y que no cambian la iimformacion
>>> tupla_1 = (1,2,3,4)
>>> tupla_1
(1, 2, 3, 4)
>>> tupla_2=1,2,3,4
>>> tupla_2
(1, 2, 3, 4)
>>> #El parentesis no siempre es necesario
>>> tupla_3=(1,)
>>> tupla_3
(1,)
>>> del tupla_1[0]
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    del tupla_1[0]
TypeError: 'tuple' object doesn't support item deletion
>>> #No se pueden borrar elementos
>>> tupla_1[0]
1
>>> tupla_4 = (1,"Pablo",[0,1,2])
>>> tupla_4
(1, 'Pablo', [0, 1, 2])
>>> #No se pueden alterar en nada
>>> #Solo a elemtos mutuables(listas) dentro pero no se pueden borrar por completo
>>> tupla_4[2][2]=3
>>> tupla_4
(1, 'Pablo', [0, 1, 3])