lista_wartości = [0, 1, 2, 3, 4]

for wartość in lista_wartości:
    # drukuj parzyste
    if wartość % 2 == 0:
        print(f'{wartość} jest parzyste')
        continue
    # wyjdź z pętli jak podzielne przez 3
    if wartość % 3 == 0:
        print(f'{wartość} jest podzielne przez 3')
        break


for i in range(5):
    print(i)
