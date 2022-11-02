import string
from Ciphers.cipher import Cipher
shift = 1
key = 'secret key'

alphabet = []
whitespace = ' '
all_alphabet_letters = string.ascii_lowercase

for character in key:
        if character not in alphabet:
            alphabet += character 

for i in all_alphabet_letters:
        if i not in alphabet:
            alphabet.append(i) 
if whitespace not in alphabet: 
        alphabet.append(whitespace)

letter_to_index = dict(zip(alphabet, range(len(alphabet))))
index_to_letter = dict(zip(range(len(alphabet)), alphabet))


def encrypt(message, shift, letter_to_index, index_to_letter):
    cipher = '' 
    for letter in message:
        number = (letter_to_index[letter] + shift) % len(letter_to_index)
        letter = index_to_letter[number]
        cipher += letter

    return cipher


def decrypt(cipher1, shift, letter_to_index, index_to_letter):
    
    decrypted = ""

    for letter in cipher1:
        number = (letter_to_index[letter] - shift) % len(letter_to_index)
        letter = index_to_letter[number]
        decrypted += letter

    return decrypted