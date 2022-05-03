"""
Typ ciąg znaków
===============

>>> a = 'hello'
>>> b = "hello"

Pisanie pojedyńczych apostrofów jest lepsze.
Czemu? - są mniej natrętne i nie trzeba naciskać "shift".
Większość programów w Python używa pojedyńczych apostrofów.

Wszystkie ciągi są w unicode (wielobajtowe znaki).


Dostęp do znaków
----------------

>>> a[0] == 'h'
True

Ciągi znaków zachowują się podobnie jak lista.

>>> a[1:]
'ello'

>>> a[::2]
'hlo'

>>> a[-1]
'o'

>>> a[::-1]
'olleh'

>>> 'll' in 'hello'
True


Wieloliniowe
------------

>>> c = '''\\
... hello
... '''

Uwaga, ten podwójny znak z opisu \\ jest pisany pojedyńczo w kodzie.

Dokumentacja
>>> \"\"\"\\
... x
... \"\"\"
'x\\n'


Znak ucieczki
-------------

Uwaga, jesteśmy w wielolinowym ciągu znaków, dlatego znak \\ jest zdublowany.
W kodzie zapisuje się go pojedyńczo.
Tutaj musimy podwójnie uciekać.


>>> e = '\\n'

Koniec linii.

>>> e = '\\t'

Tabulacja.

>>> e = '\\\\'

Znak ucieczki.
W kodzie zapisuje się ten znak \\.
Tutaj musimy podwójnie uciekać, bo jesteśmy w ciągu znaków.

>>> e = '\\x00'

Znak o numerze 0.

>>> '\\''
"'"

Apostrof w ciągu znaków.

>>> '\\N{en dash}'
'–'

Znak unicode po nazwie.

>>> '\\u2013'
'–'

Znak unicode po kodzie.

Jest więcej różnych sekwencji (python escape code).

https://docs.python.org/3/reference/lexical_analysis.html#grammar-token-python-grammar-stringescapeseq

Testy
_____


>>> '10'.isdigit()
True

>>> 'Ala'.isalpha()
True

>>> ' \t'.isspace()
True

>>> 'cześć'.islower()
True

>>> 'CZEŚĆ'.isupper()
True

>>> 'id_0'.isidentifier()
True

Adresy
------

>>> a == b
True

>>> id(a) == id(b)
True

>>> a += 'coś'
>>> b += 'coś'

>>> a == b
True

>>> id(a) == id(b)
False


Kodowanie i dekodowanie
-----------------------

>>> 'Jeść idę'.encode()
b'Je\\xc5\\x9b\\xc4\\x87 id\\xc4\\x99'

>>> b'Je\\xc5\\x9b\\xc4\\x87 id\\xc4\\x99'.decode()
'Jeść idę'

Szukanie
--------

>>> 'hello'.find('l')
2

>>> 'hello'.find('l', 3)
3

>>> 'hello'.find('l', 3, 4)
3

>>> 'hello'.endswith('lo')
True

>>> 'hello'.startswith('he')
True


Wielkość
--------

>>> 'Cześć'.lower()
'cześć'

>>> 'Cześć'.upper()
'CZEŚĆ'

>>> 'cześć'.capitalize()
'Cześć'

>>> 'dzień dobry'.title()
'Dzień Dobry'


Ścinanie
--------

>>> ' cześć '.strip()
'cześć'

>>> 'cześć!'.strip('!')
'cześć'

>>> ' cześć '.lstrip()
'cześć '

>>> ' cześć '.rstrip()
' cześć'

>>> 'prefix_infix_suffix'.removeprefix('prefix_')
'infix_suffix'

>>> 'prefix_infix_suffix'.removesuffix('_suffix')
'prefix_infix'

>>> 'prefix_infix_suffix'.replace('infix_', '')
'prefix_suffix'


Dzielenie na wyrazy
-------------------

>>> 'Dziś napisałem dwa programy!'.split()
['Dziś', 'napisałem', 'dwa', 'programy!']

>>> 'moduł.klasa.zmienna'.split('.')
['moduł', 'klasa', 'zmienna']

>>> 'moduł.klasa.zmienna'.split('.', 1)
['moduł', 'klasa.zmienna']

>>> 'moduł.klasa.zmienna'.rsplit('.', 1)
['moduł.klasa', 'zmienna']


Łączenie wyrazów
----------------

>>> wyrazy = 'Dziś napisałem dwa programy!'.split()
>>> ' '.join(wyrazy)
'Dziś napisałem dwa programy!'


Tłumaczenie znaków
------------------

>>> tablica_tłumaczeń = str.maketrans({'ł': 'l'})
>>> 'tłumaczenie'.translate(tablica_tłumaczeń)
'tlumaczenie'

>>> tablica_tłumaczeń = str.maketrans('ł', 'l')
>>> 'tłumaczenie'.translate(tablica_tłumaczeń)
'tlumaczenie'

>>> tablica_tłumaczeń = str.maketrans('ł', 'l', 'e')
>>> 'tłumaczenie'.translate(tablica_tłumaczeń)
'tlumaczni'
"""