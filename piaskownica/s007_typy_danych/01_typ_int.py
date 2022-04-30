"""
Typ całkowity
=============

>>> mała = 1
>>> wielka = 1_000_000_000_000_000_000_000_000
>>> wielka * wielka
1000000000000000000000000000000000000000000000000

W Pythonie można liczyć bardzo wielkie liczby.
Nie ma problemu z przepełnieniami i czytelnością.


Różne systemy liczbowe
----------------------

>>> 0x10
16

>>> 0o10
8

>>> 0b1
1

>>> oct(16)
'0o20'

>>> bin(16)
'0b10000'

>>> hex(16)
'0x10'


Adresy
------

>>> a = 1
>>> b = 1
>>> id(a) == id(b)
True

>>> a += 1
>>> b += 1
>>> id(a) == id(b)
True


Proste operatory
----------------

>>> a = 5
>>> b = 3

>>> -a
-5

>>> +a
5

>>> a + b
8

>>> a - b
2

>>> a * b
15


Dzielenia
---------

>>> a / b
1.6666666666666667

Wynik jest zmiennoprzecinkowy.

>>> a // b
1


Reszty
------

>>> a % b
2

>>> -a % b
1

>>> divmod(a, b)
(1, 2)


Dzybkie i skrócone przypisania
------------------------------

>>> c = 2

# c = c + 2
>>> c += 2
>>> c -= 2
>>> c *= 2
>>> c /= 2
>>> c **= 2
>>> c %= 2


Kolejność operatorów
--------------------

>>> 2 + 2 ** 2 - 3 * (4 - 5) ** 2
3


Wartość bezwzględna
-------------------

>>> abs(-5)
5


Konwersja
---------

>>> int(3.5)
3


Potęgi
------

>>> 5 ** 3
125

>>> pow(a, b)
125

Zaokrąglenia
------------

>>> import math
>>> math.trunc(5.8)
5
>>> math.floor(5.8)
5
>>> math.ceil(5.1)
6


Logika
______

>>> bool(1)
True

>>> bool(0)
False


Operacje bitowe
---------------

>>> 5 | 3
7

>>> 5 ^ 3
6

>>> 5 & 3
1

>>> 5 << 1
10

>>> 5 >> 1
2

>>> ~5
-6

>>> bin(5)
'0b101'

>>> (5).bit_length()
3

>>> (5).bit_count()
2

>>> (2048).to_bytes(4, byteorder='little')
b'\\x00\\x08\\x00\\x00'

"""

if __name__ == '__main__':
    import doctest
    doctest.testmod()
