"""
for od tyłu
===========

>>> wejście = [0, 1, 2, 3, 4, 5]
>>> wyjście = []
>>> for x in reversed(wejście):
...     wyjście.append(x + 1)
>>> print(wyjście)
[6, 5, 4, 3, 2, 1]
"""

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    