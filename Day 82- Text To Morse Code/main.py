####DICTIONARY OF ALL MORPH CODES

morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.',
    ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-',
    '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.',
    ' ': ' ',  # space
    '\n': ' ',  # newline
    '\t': ' ',  # tab
    '\r': ' ',  # carriage return
    '[': '---...', ']': '-.-.--', '{': '-.--.', '}': '-.--.-', '<': '-...-', '>': '-...-', '|': '-...-', '\\': '-...-',
    '`': '.----.', '~': '.-.-.', '_': '..--.-', '^': '..--.-'
    # Add more special characters as needed
}


def find_key_by_value(dictionary, target_value):
    for key, value in dictionary.items():
        if value == target_value:
            return key
    return None

# print(morse_code_dict["7"])
##ok

##ASK USER THE TEXT TO MORSE IT

user_text= str(input("Enter the plain text you want to morse?"))
text_to_morse=user_text.upper()


def morph_the_plain(text_to_morse):
    morphed_text= ""
    storing_morphed_text=""
    for char in text_to_morse:
        find_morph_char= morse_code_dict[char]
        morphed_text+=find_morph_char
        storing_morphed_text+=f"||{find_morph_char}"

    storing_morphed_text=storing_morphed_text[2:].split("||")
    return storing_morphed_text


MORHPED_TEXT= morph_the_plain(text_to_morse)
print(f"The equivalent morphed code is {MORHPED_TEXT}")

###UNMORPH THE MORPHED TEXT
def un_morph():
    original_text=""

    for encoded_char in MORHPED_TEXT:
        original_char= find_key_by_value(morse_code_dict,str(encoded_char))
        original_text+=str(original_char)

    print(text_to_morse)


un_morph()
