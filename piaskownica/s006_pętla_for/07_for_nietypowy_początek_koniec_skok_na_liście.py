print('for ze skakaniem')
wejście = [0, 1, 2, 3, 4, 5]
wyjście = []
for x in wejście[1:4:2]:
    wyjście.append(x)
print(wyjście)

# początek 1 element listy
# koniec 4 (bez tego elementu)
# skok 2

print('for ze skakaniem od tyłu')
wejście = [0, 1, 2, 3, 4, 5]
wyjście = []
for x in wejście[-1:-4:-2]:
    wyjście.append(x)
print(wyjście)

# początek -1 ostatni element listy
# koniec -4 (bez tego elementu)
# skok -2 (w drugą stronę)

print('for ze wycinek')
wejście = [0, 1, 2, 3, 4, 5]
wyjście = []
for x in wejście[1:4]:
    wyjście.append(x)
print(wyjście)

# początek 1 element listy
# koniec 4 (bez tego elementu)
