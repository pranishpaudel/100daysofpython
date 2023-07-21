name= "Angela"

new_list= [n*2 for n in range(1,5) if n!=2]

old_list= ["innannnn", "samirasn", "Lito", "insa","Vindasd"]

new_list= [name.upper() for name in old_list if len(name)>5]

print(new_list)


numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]


squared_numbers= [num*num for num in numbers]

print(squared_numbers)

numbers1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above

even_numbers= [n for n in numbers1 if n%2==0]

print(even_numbers)






