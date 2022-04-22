print('for wejście i wyjście')
wejście = [0, 1, 2, 3, 4, 5]
wyjście = []
for x in wejście:
    wyjście.append(x + 1)
print(wyjście)

# Krótsza i szybsza wersja.

print('krótkie for wejście i wyjście')
wejście = [0, 1, 2, 3, 4, 5]
wyjście = [x + 1 for x in wejście]
print(wyjście)

# To jest odpowiednik for powyżej.
# Różnicą jest większa ekspresja i szybkość

print('for wejście i wyjście z if')
wejście = [0, 1, 2, 3, 4, 5]
wyjście = []
for x in wejście:
    if x % 2 == 0:
        wyjście.append(x + 1)
print(wyjście)

print('krótkie for wejście i wyjście z if')
wejście = [0, 1, 2, 3, 4, 5]
wyjście = [x + 1 for x in wejście if x % 2 == 0]
print(wyjście)

# Można zapętlać.

kostka_4 = [1, 2, 3, 4]
kostka_6 = [1, 2, 3, 4, 5, 6]

wyniki = [(rzut_4, rzut_6)
          for rzut_4 in kostka_4
          for rzut_6 in kostka_6]

wyniki = []
for rzut_4 in kostka_4:
    for rzut_6 in kostka_6:
        wyniki.append((rzut_4, rzut_6))

# Zapisy są równoważne.
# Klasyczny jest czytelniejszy.
# Skrócony nieco szybszy.

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