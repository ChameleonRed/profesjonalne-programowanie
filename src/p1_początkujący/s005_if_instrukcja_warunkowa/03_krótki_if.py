"""
Krótki if zwracający wartość
============================

>>> value = True
>>> x = True if value else False
>>> print(x)
True

Zamiast:

>>> if value:
...     x = True
... else:
...     x = False
>>> print(x)
True
"""

if __name__ == '__main__':
    import doctest
    doctest.testmod()
