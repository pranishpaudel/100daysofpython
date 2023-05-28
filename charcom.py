name1 = input("Enter the first name: ")
name2 = input("Enter the second name: ")

common_characters = ''.join([char.lower() for char in name1 if char.lower() in name2.lower()])
print("Combined word:", common_characters)
