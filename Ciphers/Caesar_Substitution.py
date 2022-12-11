
def encrypt(message, shift, letter_to_index, index_to_letter):
    cipher = ""

    for letter in message:
        number = (letter_to_index[letter] + shift) % len(letter_to_index)
        letter = index_to_letter[number]
        cipher += letter

    return cipher


def decrypt(cipher, shift, letter_to_index, index_to_letter):
    decrypted = ""

    for letter in cipher:
        number = (letter_to_index[letter] - shift) % len(letter_to_index)
        letter = index_to_letter[number]
        decrypted += letter

    return decrypted


def main():
    message = input('Enter text to be encrypted: ').lower()
    shift = int(input('Enter your key(shifts): '))
    alphabet = "abcdefghijklmnopqrstuvwxy"
    letter_to_index = dict(zip(alphabet, range(len(alphabet))))
    index_to_letter = dict(zip(range(len(alphabet)), alphabet))

    cipher = encrypt(message, shift, letter_to_index, index_to_letter)
    decrypted = decrypt(cipher, shift, letter_to_index, index_to_letter)

    print('Your message: ' + message)

    print('Encrypted message: ' + cipher)

    print('Decrypted message: ' + decrypted)

main()