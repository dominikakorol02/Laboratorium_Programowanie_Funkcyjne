#Zad7

words = ["Ala", "ma", "kota", "który", "ma", "długie", "i", "pomarańczowe","futro"]

def longer_than_5(word):
    return len(word) > 5

long_words = list(filter(lambda word: len(word) > 5, words))

print(long_words)
