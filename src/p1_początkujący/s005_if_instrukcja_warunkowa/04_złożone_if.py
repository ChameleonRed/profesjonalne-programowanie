"""
Złożone warunki
===============

>>> x = True
>>> y = False
>>> z = True
>>>
>>> if (x is True
...         and (y is False
...              or z is False)):
...     print(True)
True

Lepiej takie warunki rozbijać dla czytelności.
Nie zawsze trzeba się tego trzymać na sztywno.
"""

if __name__ == '__main__':
    import doctest
    doctest.testmod()
