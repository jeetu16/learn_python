letters = ['a', 'b', 'c', 'd']

# Add item
print(letters.append('e'))
print(letters.insert(1, 'A'))
print(letters)

print("After Remove")

# Remove item
print(letters.pop())        # remove last item of list
print(letters.pop(0))       # remove given index item of list
print(letters.remove('A'))  # remove first occurance of item if found.
del letters[-1]
del letters[0:1]
letters.clear()
print(letters)
