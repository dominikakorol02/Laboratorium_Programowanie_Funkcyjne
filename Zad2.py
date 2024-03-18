#Zad2

from itertools import combinations
def wszystkie_kombinacje(elementy):
    return list(combinations(elementy,2))

przykładowa_lista = ["A","B","C","D"]

kombinacje = wszystkie_kombinacje(przykładowa_lista)

print(kombinacje)
