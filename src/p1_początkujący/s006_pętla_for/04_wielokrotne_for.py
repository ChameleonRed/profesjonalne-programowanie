"""
Wielokrotne for
===============

>>> rzuty_kostką_4 = [1, 2, 3, 4]
>>> rzuty_kostką_6 = [1, 2, 3, 4, 5, 6]

>>> for kostka_4 in rzuty_kostką_4:
...     for kostka_6 in rzuty_kostką_6:
...         print(f'{kostka_4} + {kostka_6} = {kostka_4 + kostka_6}')
1 + 1 = 2
1 + 2 = 3
1 + 3 = 4
1 + 4 = 5
1 + 5 = 6
1 + 6 = 7
2 + 1 = 3
2 + 2 = 4
2 + 3 = 5
2 + 4 = 6
2 + 5 = 7
2 + 6 = 8
3 + 1 = 4
3 + 2 = 5
3 + 3 = 6
3 + 4 = 7
3 + 5 = 8
3 + 6 = 9
4 + 1 = 5
4 + 2 = 6
4 + 3 = 7
4 + 4 = 8
4 + 5 = 9
4 + 6 = 10

"""

if __name__ == '__main__':
    import doctest
    doctest.testmod()
