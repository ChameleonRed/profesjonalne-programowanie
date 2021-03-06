"""
for sterowanie iteratorem
=========================

>>> wejście_1 = [0, 1, 2, 3, 4, 5]
>>>
>>> # tworzymy ręcznie iterator (wyręczamy for)
>>> iterator_wejście_1 = iter(wejście_1)
>>> 
>>> for x in iterator_wejście_1:
...     print(x)
...     # przeskakuj element, jeśli parzysta
...     if x % 2 == 0:
...         print('omijamy', next(iterator_wejście_1))
0
omijamy 1
2
omijamy 3
4
omijamy 5
"""

if __name__ == '__main__':
    import doctest
    doctest.testmod()
