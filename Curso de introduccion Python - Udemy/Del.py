#Del

#ayuda a borrar variables y listas
#cuidado por que una vez que se borran son dificiles de recuperar

>>> vocales ="aeiou"
>>> lista_vocales = list(vocales)
>>> lista_vocales
['a', 'e', 'i', 'o', 'u']

>>> variable_basura = "variable basura!!!"
>>> variable_basura
'variable basura!!!'
>>> del variable_basura
>>> variable_basura
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    variable_basura
NameError: name 'variable_basura' is not defined

>>> del lista_vocales[0]
>>> lista_vocales
['e', 'i', 'o', 'u']

#lo mejor igual es hacer una nueva lista y ya