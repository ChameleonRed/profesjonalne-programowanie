"""
for z generatorem
=================

>>> def generator():
...    for wyraz in 'to jest generator'.split():
...        yield wyraz


>>> for wyraz in generator():
...    print(wyraz)
to
jest
generator

Generatory:
- są wolniejsze od list
- lepiej przetwarzają potężne ilości danych (nie zużywają pamięci)
- potrafią przetwarzać zbiory nieskończone (kolejki zdarzeń)
- dają wyniki od razu po pierwszym yield
- można go przejrzeć tylko raz

>>> generator_skrócony = (wyraz for wyraz in 'to jest generator'.split())

>>> for wyraz in generator_skrócony:
...    print(wyraz)
to
jest
generator
"""

if __name__ == '__main__':
    import doctest
    doctest.testmod()
