name1 = input("Enter the first name: ")
name2 = input("Enter the second name: ")

concatenated_names = name1 + name2
common_letters = set(name1.lower()) & set(name2.lower())
num_common_letters = len(common_letters)

print("Concatenated names:", concatenated_names)
print("Number of common letters:", num_common_letters)
