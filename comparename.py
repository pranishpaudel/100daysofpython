import random

name_length = 5  # Length of the names

# Generate Name 1
name1 = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(name_length))

# Generate Name 2
name2 = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(name_length))

# Count matching letters
matching_letters = 0
for letter1, letter2 in zip(name1, name2):
    if letter1 == letter2:
        matching_letters += 1

# Print the names and matching letters
print("Name 1:", name1)
print("Name 2:", name2)
print("Matching Letters:", matching_letters)
