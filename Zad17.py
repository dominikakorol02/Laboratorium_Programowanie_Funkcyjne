#Zad17

from functools import partial

def dodaj_5(x):
  return x + 5

dodaj_5 = partial(dodaj_5, 5)

wynik = dodaj_5()

print(wynik)

