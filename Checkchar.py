import random
#Step 1 

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word= random.choice(word_list)




#TODO-2 - Ask the user to guess a letter and assign their answer to a varible called guess. Make guess lowercase.
guess= input("Enter your guess").lower()
a= chosen_word.count(guess)

if (a>=1):
  print("Right")
else:
  print("Wrong")

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.]

