#Zad19

def pobierz_dane_uzytkownika(imie, nazwisko, wiek):

  return (imie, nazwisko, wiek)

dane_uzytkownika = pobierz_dane_uzytkownika("Jan", "Kowalski", 25)

imie, nazwisko, wiek = dane_uzytkownika

print(f"Imię: {imie}")
print(f"Nazwisko: {nazwisko}")
print(f"Wiek: {wiek}")
