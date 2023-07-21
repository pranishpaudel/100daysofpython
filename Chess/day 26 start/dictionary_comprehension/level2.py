sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
sentence = "This is a sample sentence."
word_list = sentence.split()

result= {word:len(word) for word in word_list}


print(result)

