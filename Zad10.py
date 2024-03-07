#Zad10

from itertools import count

even_numbers = (2 * i for i in count())

for number in even_numbers:
    print(number)
