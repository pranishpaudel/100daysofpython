import random

name = input("Enter a name: ")
shuffled_name = random.sample(name, len(name))  # Randomly shuffle the characters
mid_index = len(name) // 2  # Calculate the middle index

output_char = shuffled_name[mid_index]  # Get the character at the middle index

print("Output character:", output_char)
