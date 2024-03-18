#Zad5

is_palindrome = lambda s: s.lower().replace(" ", "") == s[::-1].lower().replace(" ", "")
print(is_palindrome("Ten rak ma tam karnet"))  
