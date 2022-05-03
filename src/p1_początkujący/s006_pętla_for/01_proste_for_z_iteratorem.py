"""
Proste pętle w Pythonie
=======================

for w Pythonie jest bardziej ekspresywne niż w Java, C/C++, C#.
for działa na dowolnych iteratorach (coś co zwraca kolejne wartości).
Iteratorem może być: ciąg znaków, krotka, lista, zbiór, słownik, generator, wyrażenie iteracyjne, obiekt, ....
Iterowanie w for jest naturalne w Python-ie.
Indeksowanie w for jest sztuczne w Python-ie.


for z listą
-----------

>>> lista_wartości = [0, 1, 2, 3]
>>> for wartość_z_listy in lista_wartości:
...    print(wartość_z_listy)
0
1
2
3

To samo w C++:

#include <iostream>
#include <vector>

int main()
{
    std::vector<int> v = {0, 1, 2, 3, 4, 5};
    for (auto n : v) {
        std::cout << n << std::endl;
    }
}

To samo w Javie:

import java.util.List;
import java.util.ArrayList;

class Main {
    public static void main(String[] args) {
        List<Integer> lista_wartosci = new ArrayList<>(List.of(0, 1, 2, 3, 4, 5));
        for (var wartosc_z_listy: lista_wartosci) {
            System.out.println(wartosc_z_listy);
        }
    }
}


for z ciągiem znaków
--------------------

>>> for wartość_z_listy in 'ciąg':
...    print(wartość_z_listy)
c
i
ą
g

To samo w C++

#include <iostream>
#include <string>
 
int main()
{
    std::wstring v = L"ciąg";

    for (auto x : v) {
        std::wcout << x << std::endl;
    }
}


for z wyrazami
--------------

>>> for wyraz in 'lista wartości'.split():
...    print(wyraz)
lista
wartości

Prawie to samo w C++.

#include <iostream>
#include <vector>
#include <string>

int main()
{
    std::vector<std::string> v = { "lista", "wartości" };

    for (auto wyraz : v) {
        std::cout << wyraz << std::endl;
    }
}


Wzorzec akumulator
------------------

>>> wartości = [1, 2, 3, 4]
>>> akumulator = 0
>>> for x in wartości:
...     akumulator += x

>>> akumulator
10

Wzorzec nie jest poprawny, bo:

>>> sum(wartości)
10


Wzorzec min i max
-----------------

>>> wartości = [1, 2, 3, 4]
>>> najmniejsza = wartości[0] if wartości else None
>>> największa = wartości[0] if wartości else None
>>> for x in wartości[1:]:
...     if x > największa:
...         największa = x
...     if x < najmniejsza:
...         najmniejsza = x

>>> najmniejsza
1

>>> największa
4

Wzorzec nie jest poprawny, bo:

>>> min(wartości)
1

>>> max(wartości)
4

Podobnie jest ze średnią, bo:

>>> sum(wartości) / len(wartości)
2.5


"""

if __name__ == '__main__':
    import doctest
    doctest.testmod()
