"""
if warunki
==========

Bez warunków nie ma if.
Wartość warunku wylicza się bool(x).

Prawda
------

>>> True
True

Fałsz
-----

>>> False
False

Zaprzeczenie
------------

>>> not True
False

Lub (alternatywa)
-----------------

>>> True or False
True

I (koniunkcja)
--------------

>>> True and False
False

Pusta lista
-----------

>>> bool([])
False

Pusta krotka
------------

>>> bool(())
False

Pusty słownik
-------------

>>> bool({})
False

Pełna krotka
------------

>>> bool((0,))
True

Pełna lista
-----------

>>> bool([0])
True

Liczba elementów na liście
--------------------------

>>> bool(len([0]) == 1)
True

Wszystkie na liście
-------------------

>>> bool(all(x >= 1 for x in [1, 2, 3]))
True

Żaden na liście
---------------

>>> bool(all(x != 0 for x in [1, 2, 3]))
True

Żaden parzysty na liście
------------------------

>>> bool(all(x != 0 for x in [1, 2, 3] if x % 2 == 0))
True

Podzielny przez 3
-----------------
>>> bool(9 % 3 == 0)
True

Pełen słownik
-------------

>>> bool({False: False})
True

Pusty zbiór
-----------

>>> bool(set())
False

Pełen zbiór
-----------

>>> bool({1})
True

Brak wartości
-------------

>>> bool(None)
False

Jedynka całkowita
-----------------

>>> bool(1)
True

Jedynka zmiennoprzecinkowa
--------------------------
>>> bool(1.0)
True

Zero całkowite
--------------

>>> bool(0)
False

Zero zmiennoprzecinkowe
-----------------------

>>> bool(0.0)
False

Większe
-------

>>> bool(1 > 0)
True

Większe równe
-------------

>>> bool(1 >= 0)
True

Równe
-----

>>> bool(1 == 0)
False

Różne
-----

>>> bool(1 != 0)
True

2 w przedziale (1, 3)
---------------------

>>> bool(1 < 2 < 3)
True

obiekt powstał z listy
----------------------

>>> isinstance([], list)
True

Klasa dziedziczy z listy
------------------------

>>> issubclass(list, list)
True

Stałe mają ten sam adres
------------------------

>>> id([]) == id([])
True

Zmienne mają ten sam adres
--------------------------

>>> id(list()) == id(list())
False

listy mają te same wartości
---------------------------

>>> [1, 2] == [1, 2]
True

Listy mają te same wartości
---------------------------

>>> list([1, 2]) == list([1, 2])
True

Ciągi znaków są te same
-----------------------

>>> 'a' == 'a'
True

Stałe mają ten sam adres
------------------------

>>> id('a') == id('a')
True

Liczby urojone są takie same
----------------------------

>>> 3 + 2j == 3 + 2j
True

"""