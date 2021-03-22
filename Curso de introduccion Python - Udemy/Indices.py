#indices
>>> #Las listas y las cadenas se parecen mucho
>>> #Pero vamos a los indices
>>> alfabeto ="abcdefghijklmnñopqstuvwxyz"
>>> alfabeto
'abcdefghijklmnñopqstuvwxyz'
>>> alfabeto_lista=list(alfabeto)
>>> alfabeto_lista
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
>>> #cada elemento tiene un numero asociado por ejemplo a1 b2 c3
>>> #para saberlo se usa
>>> alfabeto_lista.index("a")
0
>>> alfabeto_lista.index("c")
2
>>> alfabeto_lista.index("x")
23
>>> alfabeto.index("a")
0
>>> alfabeto.index("c")
2

>>> alfabeto.index("cd")
2
>>> alfabeto_lista[10]
'k'
>>> alfabeto[11]
'l'
#tambien se puede encontrar con numeros negativos osea se cuenta alreves
>>> alfabeto_lista[24]
'y'
>>> alfabeto_lista[-2]
'y'
>>>