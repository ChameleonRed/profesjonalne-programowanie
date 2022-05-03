"""
For skoki
=========

>>> wejście = [0, 1, 2, 3, 4, 5]
>>> for x in wejście:
...     # pomiń parzyste
...     if x % 2 == 0:
...         print(f'{x} pomiń')
...         continue
...     if x == 3:
...         print(f'{x} skończ')
...         break
0 pomiń
2 pomiń
3 skończ

Alternatywą jest też return.

>>> def funkcja(wejście):
...     for x in wejście:
...         # pomiń parzyste
...         if x % 2 == 0:
...             print(f'{x} pomiń')
...             continue
...         if x == 3:
...             print(f'{x} skończ')
...             return
>>> funkcja(wejście)
0 pomiń
2 pomiń
3 skończ


Można też przez raise choć mniej naturalne.

>>> try:
...     for x in wejście:
...         # pomiń parzyste
...         if x % 2 == 0:
...             print(f'{x} pomiń')
...             continue
...         if x == 3:
...             print(f'{x} skończ')
...             raise StopIteration()
... except StopIteration:
...     pass
0 pomiń
2 pomiń
3 skończ


"""