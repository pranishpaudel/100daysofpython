import random

def mix_names(name1, name2):
    mixed_name = name1 + name2
    mixed_name = list(mixed_name)
    random.shuffle(mixed_name)
    mixed_name = ''.join(mixed_name)
    return mixed_name

# Get user input
name1 = input("Enter the first name: ")
name2 = input("Enter the second name: ")

# Call the function and get the mixed name
mixed_name = mix_names(name1, name2)

# Print the mixed name
print("Mixed Name:", mixed_name)
