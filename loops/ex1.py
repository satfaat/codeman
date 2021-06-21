""" Python 2 syntax """
for i in [1, 2, 3]:
  print(i)

for ch in "Hi!":
  print(ch)

for num in range(5):
  print('Rocks!')

vowels = ['a', 'e', 'i', 'o', 'u']
word = input("Provide a word to search for volwels: ")

for letter in word:
  if letter in vowels:
    if letter not in found:
      found.append(letter)
for vowel in found:
  print(letter)
