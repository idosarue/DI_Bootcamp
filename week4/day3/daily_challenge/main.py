import string

alphabet = list(string.ascii_lowercase)
text = input('Enter a sentence: ').lower()
new_text = list(text.replace(" ", ""))
print(new_text)
answer = input("encrypt or decrypt? ").lower()


def encrypt():
    shift = int(input("enter shift: "))
    for letter in new_text:
        new_letter = alphabet.index(letter)
        if (new_letter + shift) < len(alphabet):
            letter = alphabet[new_letter + shift]
        else:
            letter = alphabet[(new_letter + shift) - len(alphabet)]

        print(letter, end="")


def decrypt():
    shift = int(input("enter shift: "))
    for letter in new_text:
        new_letter = alphabet.index(letter)
        letter = alphabet[new_letter - shift]
        print(letter, end="")


if answer == "encrypt":
    encrypt()
elif answer == "decrypt":
    decrypt()
else:
    print('command not recognized')