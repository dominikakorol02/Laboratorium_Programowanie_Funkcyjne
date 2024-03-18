#Zad1

import itertools

litery1 = ['A', 'B']
litery2 = ['C', 'D']

kombinacje = itertools.product(litery1, litery2)

for kombinacja in kombinacje:
    print(kombinacja)