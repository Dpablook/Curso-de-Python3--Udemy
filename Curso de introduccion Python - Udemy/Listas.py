#Listas en Python
#Las listas sirven para agrupar elementos de datos , son un conjunto de objetos

[1,2,3,4,5]
>>> [1,2,3,4,5]
[1, 2, 3, 4, 5]
>>> Lista = [1,2,3,4,5]
>>> Lista
[1, 2, 3, 4, 5]
>>> Lista + 5
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    Lista + 5
TypeError: can only concatenate list (not "int") to list
>>> Lista + [5,6]
[1, 2, 3, 4, 5, 5, 6]

 #Una lista se suma a otra lista
>>> Lista = Lista + [6,7]
>>> Lista
[1, 2, 3, 4, 5, 6, 7]
>>> Lista += [8,9]
>>> Lista
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> Lista * 5
[1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> Lista.append(10)
>>> Lista
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> #Para agregar un numero
>>> Lista.append("Pablo")
>>> Lista
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Pablo']
>>> Lista.append([11,12,13])
>>> Lista
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Pablo', [11, 12, 13]]


>>> lista_2 = [1,2,3,4,5]
>>> lista_2
[1, 2, 3, 4, 5]
>>> lista_2.append(6)
>>> lista_2
[1, 2, 3, 4, 5, 6]
>>> #hasta aca solo se puede agragar un elemento
>>> lista_2.extend([7,8])
>>> lista_2
[1, 2, 3, 4, 5, 6, 7, 8]
>>> #para remover un elemento
>>> lista_2.remove(8)
>>> lista_2
[1, 2, 3, 4, 5, 6, 7]
>>>


