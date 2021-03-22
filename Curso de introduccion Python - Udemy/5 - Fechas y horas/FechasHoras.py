#Fechas y horas en Python

>>> import datetime
>>> dir(datetime)
['MAXYEAR', 'MINYEAR', '_EPOCH', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'date', 'datetime', 'datetime_CAPI', 'time', 'timedelta', 'timezone', 'tzinfo']
>>> datetime.datetime.now()
datetime.datetime(2020, 9, 3, 15, 47, 5, 500000)
>>> #Conseguimos la fecha,la hora y fecha.
>>> now = datetime.datetime.now()
>>> now
datetime.datetime(2020, 9, 3, 15, 48, 30, 734375)
>>> now
datetime.datetime(2020, 9, 3, 15, 48, 30, 734375)
>>> now.day
3
>>> now.minute
48
>>> now.year
2020

>>> now.replace(minute=0)
datetime.datetime(2020, 9, 3, 15, 0, 30, 734375)
>>> now= now.replace(minute=0,second=0,microsecond=0)
>>> now
datetime.datetime(2020, 9, 3, 15, 0)
>>> tiempo_transcurrido = datetime.datetime.now() - now
>>> tiempo_transcurrido
datetime.timedelta(0, 3154, 93750)

>>> #dias,segundos y microsegundos
>>> #genera un cambio en los numeros
>>> tiempo_transcurrido.seconds / 60
52.56666666666667