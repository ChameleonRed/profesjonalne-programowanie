"""
Szybkie i skrócone for
======================


for wejście i wyjście
---------------------

>>> wejście = [0, 1, 2, 3, 4, 5]
>>> wyjście = []
>>> for x in wejście:
...     wyjście.append(x + 1)
>>> print(wyjście)
[1, 2, 3, 4, 5, 6]


krótkie for wejście i wyjście
-----------------------------

>>> wejście = [0, 1, 2, 3, 4, 5]
>>> wyjście = [x + 1 for x in wejście]
>>> print(wyjście)
[1, 2, 3, 4, 5, 6]

To jest odpowiednik for powyżej.
Różnicą jest większa ekspresja i szybkość


for wejście i wyjście z if
--------------------------

>>> wejście = [0, 1, 2, 3, 4, 5]
>>> wyjście = []
>>> for x in wejście:
...     if x % 2 == 0:
...         wyjście.append(x + 1)
>>> print(wyjście)
[1, 3, 5]


krótkie for wejście i wyjście z if
----------------------------------

>>> wejście = [0, 1, 2, 3, 4, 5]
>>> wyjście = [x + 1 for x in wejście if x % 2 == 0]
>>> print(wyjście)
[1, 3, 5]

Wielokrotne skrócone for
------------------------

>>> kostka_2 = [1, 2]
>>> kostka_4 = [1, 2, 3, 4]
>>>
>>> wyniki = [(rzut_2, rzut_4)
...           for rzut_2 in kostka_2
...           for rzut_4 in kostka_4]
>>> print(wyniki)
[(1, 1), (1, 2), (1, 3), (1, 4), (2, 1), (2, 2), (2, 3), (2, 4)]

>>> wyniki = []
>>> for rzut_2 in kostka_2:
...     for rzut_4 in kostka_4:
...         wyniki.append((rzut_2, rzut_4))
>>> print(wyniki)
[(1, 1), (1, 2), (1, 3), (1, 4), (2, 1), (2, 2), (2, 3), (2, 4)]

Zapisy są równoważne.
Klasyczny jest czytelniejszy.
Skrócony nieco szybszy.

Sprawdź co jest szybsze.

import timeit

kostka_4 = [1, 2, 3, 4]
kostka_6 = [1, 2, 3, 4, 5, 6]


def krótszy():
    wyniki = [(rzut_4, rzut_6)
              for rzut_4 in kostka_4
              for rzut_6 in kostka_6]


def dłuższy():
    wyniki = [(rzut_4, rzut_6)
              for rzut_4 in kostka_4
              for rzut_6 in kostka_6]


print(timeit.timeit(krótszy))
print(timeit.timeit(dłuższy))
"""

if __name__ == '__main__':
    import doctest
    doctest.testmod()
