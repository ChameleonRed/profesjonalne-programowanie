"""
Wielokrotne if
==============

>>> if True:
...     if True:
...         print(True)
True

Odpowiednik:

if (1) {
    if (1) {
        print(1);
    }
}
"""

if __name__ == '__main__':
    import doctest
    doctest.testmod()
