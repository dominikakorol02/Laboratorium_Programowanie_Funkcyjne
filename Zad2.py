# Zad2

def make_multiplier(m):
  def multiply(x):
    return x * m

  return multiply

multiplier_2 = make_multiplier(2)
multiplier_3 = make_multiplier(3)

print(multiplier_2(6))
print(multiplier_3(5))
