"""
for ze skakaniem
================

for ze skakaniem do przodu
--------------------------

>>> wejście = [0, 1, 2, 3, 4, 5]
>>> wyjście = []
>>> for x in wejście[1:4:2]:
...     wyjście.append(x)
>>> print(wyjście)
[1, 3]

początek 1 element listy
koniec 4 (bez tego elementu)
skok 2

for ze skakaniem od tyłu
------------------------

>>> wejście = [0, 1, 2, 3, 4, 5]
>>> wyjście = []
>>> for x in wejście[-1:-4:-2]:
...     wyjście.append(x)
>>> print(wyjście)
[5, 3]

początek -1 ostatni element listy
koniec -4 (bez tego elementu)
skok -2 (w drugą stronę)

for z wycinka
-------------

>>> wejście = [0, 1, 2, 3, 4, 5]
>>> wyjście = []
>>> for x in wejście[1:4]:
...     wyjście.append(x)
>>> print(wyjście)
[1, 2, 3]

początek 1 element listy
koniec 4 (bez tego elementu)

"""

if __name__ == '__main__':
    import doctest
    doctest.testmod()
