#Zad11

def sort_by_length(strings):
    return sorted(strings, key=lambda s: len(s))

strings = ["Fizjoterapia", "to", "nauka", "o", "metodach", "leczenia", "środkami", "naturalnymi"]
sorted_strings = sort_by_length(strings)
print(sorted_strings)
