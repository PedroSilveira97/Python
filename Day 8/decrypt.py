from alphabet import alphabet


def decrypt_message(message, shift_amount):
    decrypted_message = ""
    for char in message:
        if char in alphabet:
            i = (alphabet.index(char) - shift_amount)%len(alphabet)
            decrypted_message = decrypted_message + alphabet[i]
        else:
            decrypted_message = decrypted_message + char
    return decrypted_message