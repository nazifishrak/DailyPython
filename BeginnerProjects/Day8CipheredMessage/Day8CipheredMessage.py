from letters import alphabet
import letters
print(letters.logo)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
# defaulted to 5
# shift = int(input("Type the shift number:\n"))


def encrypt(plain_text: str, shift_amount: int =5) -> str:
    encrypted_message=""
    for i in plain_text:
        if i in alphabet:
            shifted_i_index = alphabet.index(i) + shift_amount
            encrypted_message+=alphabet[shifted_i_index]
        else:
            encrypted_message += i
    
    return f"""\n****Your encrypted message is ****\n{encrypted_message}"""


def decrypt(plain_text: str, shift_amount: int = 5) -> str:
    decrypted_message=""
    for i in plain_text:
        if i in alphabet:
            shifted_i_index = alphabet.index(i) - shift_amount
            decrypted_message+=alphabet[shifted_i_index]
        else:
            decrypted_message += i
    
    return f"""\n****The secret message was****\n{decrypted_message}"""

if direction == "encode":
    print(encrypt(text))
elif direction == "decode":
    print(decrypt(text))
else:
    print("Invalid option")
