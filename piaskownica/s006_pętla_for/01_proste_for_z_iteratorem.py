# for w Pythonie jest bardziej ekspresywne niż w Java, C/C++, C#
# for działa na dowolnych iteratorach (coś co zwraca kolejne wartości)
# iteratorem może być ciąg znaków, krotka, lista, zbiór, słownik, generator, wyrażenie iteracyjne, obiekt, ...

print('for z listą')
lista_wartości = [0, 1, 2, 3, 4, 5]
for wartość_z_listy in lista_wartości:
    print(wartość_z_listy)

# to jest odpowiednik
# int lista = {0, 1, 2, 3, 4, 5};
#
# for (int i = 0; i < 10; ++i)
# {
#   print(lista[i]);
# }
#
# indeksowanie jest sztuczny w Python
# iterowanie jest naturalne w Python

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


def generator():
    for wyraz in 'to jest generator'.split():
        yield wyraz


for wyraz in generator():
    print(wyraz)

# Ten idiom Pythona nie ma odpowiedników.
# Choć można go próbować implementować.
