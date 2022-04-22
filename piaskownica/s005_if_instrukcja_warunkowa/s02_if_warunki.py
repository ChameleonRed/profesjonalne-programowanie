# Bez warunków nie ma if.
# Wartość warunku wylicza się bool(x).

warunki = (
    ('prawda', 'True'),
    ('zaprzeczenie', 'not True'),
    ('lub (alternatywa)', 'True or False'),
    ('i (koniunkcja)', 'True and False'),
    ('fałsz', 'False'),
    ('pusta lista', '[]'),
    ('pusta słownik', '{}'),
    ('pusta zbiór', 'set()'),
    ('brak wartości', 'None'),
    ('sprawdzenie typu lista', '[] is None'),
    ('nie zero', '1'),
    ('zero', '0'),
    ('nie zero', '1.0'),
    ('zero', '0.0'),
    ('równe', '1 == 1.0'),
    ('większe', '1 > 1.0'),
    ('większe równe', '1 >= 1.0'),
    ('nierówne', '1 != 1.0'),
    ('sprawdzenie typu', '[] is list'),
    ('sprawdzenie typu', '{} is dict'),
    ('sprawdzenie typu', '{1: 1} is dict'),
    ('sprawdzenie typu', '{1,} is set'),
    ('czy obiekt dziedziczy z klasy', 'isinstance([], list)'),
    ('czy klasa dziedziczy z klasy', 'issubclass(list, list)'),
    ('czy to te same obiekty', 'id(list()) == id(list())'),
    ('czy to te same obiekty (uwaga stała!)', 'id([]) == id([])'),
    ('czy to obiekty o tej same wartości', '[] == list()'),
    ('czy te same ciągi znaków', '\'a\' == \'a\'')
)

for opis, warunek in warunki:
    print(opis, warunek, '->', eval(warunek))
    print('typ =', eval(f'type({warunek})'))
    print()
