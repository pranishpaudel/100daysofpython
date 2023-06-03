programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.", 
  "Function": "A piece of code that you can easily call over and over again."}

#Loop in dictionary
for value in programming_dictionary:
  print (value)
  
#Adding a value and key in dictionary
programming_dictionary["Loop"]="Repeated execution of program"
print(programming_dictionary)

#Clearing a dictorinary
empty_dictionary={}
programming_dictionary= {}
print(programming_dictionary)

#Edit an item in a dictionary

programming_dictionary["Bug"]="Its a insect lol"
print(programming_dictionary)


