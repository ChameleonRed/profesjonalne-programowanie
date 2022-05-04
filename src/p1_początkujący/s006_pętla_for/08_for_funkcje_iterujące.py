"""
funkcje iterujące
=================


for od tyłu
-----------

>>> wejście = [0, 1, 2, 3, 4, 5]
>>> wyjście = []
>>> for x in reversed(wejście):
...     wyjście.append(x + 1)
>>> print(wyjście)
[6, 5, 4, 3, 2, 1]


for numerowanie elementów
-------------------------

>>> wejście = [0, 1, 2, 3, 4, 5]
>>> for indeks, wartość in enumerate(wejście):
...     print(indeks, wartość)
0 0
1 1
2 2
3 3
4 4
5 5

for parowanie danych
--------------------

>>> wejście_1 = [0, 1, 2, 3, 4, 5]
>>> wejście_2 = [0, 1, 2, 3, 4, 5]
>>> wyjście = []
>>>
>>> for x1, x2 in zip(wejście_1, wejście_2):
...     wyjście.append(x1 + x2)
>>> print(wyjście)
[0, 2, 4, 6, 8, 10]
"""

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    