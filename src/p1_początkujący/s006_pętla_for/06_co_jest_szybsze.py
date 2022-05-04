"""
Sprawdź, co jest szybsze!
"""

import timeit

kostka_4 = [1, 2, 3, 4]
kostka_6 = [1, 2, 3, 4, 5, 6]


def krótszy():
    wyniki = [(rzut_4, rzut_6)
              for rzut_4 in kostka_4
              for rzut_6 in kostka_6]
    return wyniki


def dłuższy():
    wyniki = []
    for rzut_4 in kostka_4:
        for rzut_6 in kostka_6:
            wyniki.append((rzut_4, rzut_6))
    return wyniki


if __name__ == '__main__':
    print(timeit.timeit(krótszy))
    print(timeit.timeit(dłuższy))
