# for w Pythonie jest bardziej ekspresywne niż w Java, C/C++, C#
# for działa na dowolnych iteratorach (coś co zwraca kolejne wartości)
# iteratorem może być ciąg znaków, krotka, lista, zbiór, słownik, generator, wyrażenie iteracyjne, obiekt, ...

print('for z zasięgiem (0, koniec)')
for i in range(10):
    print(i)

# Wynik powyżej odpowiada:
# for (int i = 0; i < 10; ++i)
# {
#   print(i);
# }
#
# Indeksowanie jest sztuczne w Python.
# Iterowanie jest naturalne w Python.

print('for z zasięgiem (początek, koniec)')
for i in range(2, 10):
    print(i)

# początek = 2
# koniec = 10 (bez 10)
#
# wynik powyżej odpowiada
# for (int i = 2; i < 10; ++i)
# {
#   print(i);
# }


print('for z zasięgiem (początek, koniec, skok)')
for i in range(2, 10, 2):
    print(i)
