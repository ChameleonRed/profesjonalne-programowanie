"""
for z zasięgami
===============

for z zasięgiem (0, koniec)
---------------------------

>>> for i in range(3):
...     print(i)
0
1
2

Odpowiednik pseudo Java/C++:
for (int i = 0; i < 10; ++i)
{
  print(i);
}


for z zasięgiem (początek, koniec)
__________________________________

>>> for i in range(2, 5):
...     print(i)
2
3
4

początek = 2
koniec = 10 (bez 10)

Odpowiednik pseudo Java/C++:
for (int i = 2; i < 10; ++i)
{
  print(i);
}


for z zasięgiem (początek, koniec, skok)
________________________________________

>>> for i in range(2, 6, 2):
...     print(i)
2
4

Odpowiednik pseudo Java/C++:
for (int i = 2; i < 6; i += 2)
{
  print(i);
}

"""

if __name__ == '__main__':
    import doctest
    doctest.testmod()
