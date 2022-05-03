"""
for z else
==========

for z else jest Python-owym idiomem.
Użycie jest rzadkie, ale upraszcza kod.


for z else i break
------------------

>>> for i in range(10):
...     break
... else:
...     print('Never printed if break.')

# Nie trzeba definiować flagi przy break jest else.


for z else bez break
--------------------

>>> for i in range(10):
...     continue
... else:
...     print('Never printed if break.')
Never printed if break.

Jak nie ma break else nie ma sensu.
"""

if __name__ == '__main__':
    import doctest
    doctest.testmod()
