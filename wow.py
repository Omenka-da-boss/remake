import random
import string

char = " " + string.ascii_letters + string.digits + string.punctuation

char  = list(char)

key  = char.copy()

random.shuffle(key)

# ENCRYPTION

plain_text = input("Enter letter you want to encrypt: ")
cipher_text = ""

for letter in plain_text:
    # here the index variable is the index of each character on the char list
    index  = char.index(letter)
    # Now we add the to the cipher text each random value gotten from the key list
    cipher_text += key[index]

print(f"Plain_text: {plain_text}")
print(f"Cipher_text: {cipher_text}")


# DECRYTPTION
cipher_text = input("Enter text to decrypt: ")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plain_text += char[index]
    
print(f"Cipher_Text: {cipher_text}")
print(f"Plain_text: {plain_text}")