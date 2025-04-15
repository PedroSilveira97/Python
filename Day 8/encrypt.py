from alphabet import alphabet


def encrypt_message(message, shift_amount):
    encrypted_message = ""
    for char in message:
            if char in alphabet:
                i = (alphabet.index(char) + shift_amount)%len(alphabet)
                encrypted_message = encrypted_message + alphabet[i]
            else:
                encrypted_message = encrypted_message + char
    return encrypted_message
