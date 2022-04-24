"""
for numerowanie elementów
=========================

>>> wejście = [0, 1, 2, 3, 4, 5]
>>> for indeks, wartość in enumerate(wejście):
...     print(indeks, wartość)
0 0
1 1
2 2
3 3
4 4
5 5
"""

if __name__ == '__main__':
    import doctest
    doctest.testmod()
