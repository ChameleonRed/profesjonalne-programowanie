# for w Pythonie jest bardziej ekspresywne niż w Java, C/C++, C#.
# for działa na dowolnych iteratorach (coś co zwraca kolejne wartości).
# Iteratorem może być ciąg znaków, krotka, lista, zbiór, słownik, generator, wyrażenie iteracyjne, obiekt, ....
# Indeksowanie jest sztuczne w Python-ie.
# Iterowanie jest naturalne w Python-ie.

print('for z listą')

lista_wartości = [0, 1, 2, 3, 4, 5]
for wartość_z_listy in lista_wartości:
    print(wartość_z_listy)

# Tak to wygląda w C++:

'''
#include <iostream>
#include <vector>

int main()
{
    std::vector<int> v = {0, 1, 2, 3, 4, 5};
    for (int n : v) {
        std::cout << n << std::endl;
    }
}
'''

# Tak to wygląda w Javie:

'''
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
'''

print('for z ciągiem znaków')

for wartość_z_listy in 'lista wartości':
    print(wartość_z_listy)

# To jest odpowiednik:
# int ciag = "lista wartości";
#
# for (int i = 0; i < 10; ++i)
# {
#   print(ciag[i]);
# }

print('for z wyrazami')

for wyraz in 'lista wartości'.split():
    print(wyraz)

# To jest odpowiednik, choć bez kodu tnącego na wyrazy.
#
# int wyrazy = {"lista", "wartości"};
#
# for (int i = 0; i < 10; ++i)
# {
#   print(wyrazy[i]);
# }
#
# Ewentualnie np. w nowoczesnym C++.
#
# #include <iostream>
# #include <vector>
# #include <string>
#
# int main()
# {
#     std::vector<std::string> v = { "lista", "wartości" };
#
#     for (auto n : v) {
#         std::cout << n << std::endl;
#     }
# }

print('for z generatorem')

def generator():
    for wyraz in 'to jest generator'.split():
        yield wyraz


for wyraz in generator():
    print(wyraz)

