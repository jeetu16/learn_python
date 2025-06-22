letters = ['a', 'b', 'c', 'd', 'e']

for letter in letters:
    print(letter)

for letter in enumerate(letters):
    print(letter[0], letter[1])

for index, letter in enumerate(letters):
    print(index, letter)
