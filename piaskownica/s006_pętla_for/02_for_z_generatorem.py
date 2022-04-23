def generator():
    for wyraz in 'to jest generator'.split():
        yield wyraz


for wyraz in generator():
    print(wyraz)

# Generatory:
# - są wolniejsze od list
# - lepiej przetwarzają potężne ilości danych (nie zużywają pamięci)
# - potrafią przetwarzać zbiory nieskończone (kolejki zdarzeń)
# - dają wyniki od razu po pierwszym yield
# - można go przejrzeć tylko raz

generator_skrócony = (wyraz for wyraz in 'to jest generator'.split())

for wyraz in generator():
    print(wyraz)
