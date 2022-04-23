wejście_1 = [0, 1, 2, 3, 4, 5]
wejście_2 = [0, 1, 2, 3, 4, 5]
wyjście = []

for x1, x2 in zip(wejście_1, wejście_2):
    wyjście.append(x1 + x2)
print(wyjście)
