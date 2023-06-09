# Describe Problem
def my_function():
  for i in range(1, 20):
    if i == 20:
      print("You got it")
my_function()


# IDENTIFY THE Bugg
#rewriting the code
def my_function():
  for i in range(1, 21):
    if i == 20:
      print("You got it")
my_function()

#since inside loop it excludes the last value