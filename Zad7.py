#Zad7

from itertools import groupby

def parzystosc(liczba):
  return liczba % 2 == 0

liczby = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for klucz, grupa in groupby(liczby, parzystosc):
  print(f"Klucz: {klucz}, Grupa: {list(grupa)}")
