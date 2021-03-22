#Split and Join
>>> #Las cadenas de texto son un conjunto de letras
>>> #Se pueden crear listas con el metodo list()
>>> list([1,2,3,4,5])
[1, 2, 3, 4, 5]
>>> list("pablo")
['p', 'a', 'b', 'l', 'o']
>>> list("youtube")
['y', 'o', 'u', 't', 'u', 'b', 'e']
>>> listas_letras = list ("youtube")
>>> listas_letras
['y', 'o', 'u', 't', 'u', 'b', 'e']
>>> listas_letras + list ("es genial")
['y', 'o', 'u', 't', 'u', 'b', 'e', 'e', 's', ' ', 'g', 'e', 'n', 'i', 'a', 'l']
>>> #hasta aca lo de listas
>>> #pero tambien tenemos el metodo split
>>> "Pablo".split()
['Pablo']
>>> #Eso pone mi nombre como elemento de una lista
>>> #lo que tiene de diferente es que lo pone todo junto y no con letras separadas
>>> "Hola como estas".split()
['Hola', 'como', 'estas']
>>> "Carne,pollo,fideos,pizza".split()
['Carne,pollo,fideos,pizza']
>>> comida_favorita= "Carne,pollo,fideos,pizza"
>>> comida_favorita
'Carne,pollo,fideos,pizza'
>>> comida_favorita.split(",")
['Carne', 'pollo', 'fideos', 'pizza']
>>> #El metodo join es el opuesto al split
>>> lista_comida_favorita = ['Carne', 'pollo', 'fideos', 'pizza']
>>> lista_comida_favorita
['Carne', 'pollo', 'fideos', 'pizza']
>>> ",".join(lista_comida_favorita)
'Carne,pollo,fideos,pizza'
>>> ", ".join(lista_comida_favorita)
'Carne, pollo, fideos, pizza'
>>> #Se le agrega una coma o una coma + espacio
>>> "Mi comida favorita es: " + ", ".join(lista_comida_favorita)
'Mi comida favorita es: Carne, pollo, fideos, pizza'
>>>
