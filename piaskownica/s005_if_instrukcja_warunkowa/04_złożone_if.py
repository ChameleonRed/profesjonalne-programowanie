x = True
y = False
z = True

if (x is True
        and (y is False
             or z is False)):
    print(True)

# Lepiej takie warunki rozbijać dla czytelności.
# Nie zawsze trzeba się tego trzymać na sztywno.
