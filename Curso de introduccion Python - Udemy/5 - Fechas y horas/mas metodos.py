#Mas metodos

#Today y Now

#Formateando Fechas

>>> import datetime
>>> now = datetime.datetime.now
>>> now
<built-in method now of type object at 0x1E239D18>
>>> now = datetime.datetime.now()
>>> now
datetime.datetime(2020, 9, 3, 16, 6, 31, 671875)
>>> now.strftime("%B %d, %Y")
'September 03, 2020'
>>> #Podemos buscar en la documentacion los codigos con los distintos formatos   de fechas.
>>>

#Zonas Horarias

>>> import datetime
>>> central_time = datetime.timezone(datetime.timedelta(hours = -6))
>>> central_time
datetime.timezone(datetime.timedelta(-1, 64800))
>>> pacific_time = datetime.timezone(datetime.timedelta(hours = -8))
>>> pacific_time
datetime.timezone(datetime.timedelta(-1, 57600))
>>>

#Las horas para restar las tenes que buscar :(



