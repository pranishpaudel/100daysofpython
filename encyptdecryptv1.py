alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def runtime(main_text, shift_amount, direction_num):
    if (direction_num == "encode"):
        encyptword = ""
        for letter in main_text:
            char = alphabet[(alphabet.index(letter) + shift_amount) % len(alphabet)]
            encyptword += char

        print(encyptword)
    else:
        decyptword = ""
        for letter in main_text:
            char = alphabet[(alphabet.index(letter) - shift_amount) % len(alphabet)]
            decyptword += char

        print(decyptword)

runtime(main_text=text, shift_amount=shift, direction_num=direction)
