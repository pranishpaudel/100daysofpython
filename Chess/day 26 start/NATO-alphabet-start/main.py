import pandas as pd

is_done= False
while not is_done:

    # TODO 1. Create a dictionary in this format:
    file = open("Chess/day 26 start/NATO-alphabet-start/nato_phonetic_alphabet.csv")
    data = pd.read_csv(file)  # Use pd.read_csv() to read the CSV file into a DataFrame
    file.close()  # Close the file after reading the data

    new_dict = {row.letter: row.code for (index, row) in data.iterrows()}

    # TODO 2. Create a list of the phonetic code words from a word that the user inputs.

    user_word = input("Enter a word to get its phonetic code: ").upper()

    is_numeric= False
    for letter in user_word:
        if letter.isnumeric() == True:
            is_numeric= True

    try:
        if is_numeric:
            raise(ValueError("Numeric value"))
    except:
            print("Only alphabet accepted")
        
    else:
        phonetic= [new_dict[letter] for letter in user_word if letter in new_dict]
        print(phonetic)
        is_done= True


