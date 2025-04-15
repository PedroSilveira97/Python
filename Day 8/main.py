import decrypt
import encrypt
message = str(input("What is your message? ")).lower()
operation = str(input("Do you want to encrypt or decrypt the message? ")).lower()
shift_amount = int(input("What is the desired shift amount? "))
if operation == "encrypt":
    print(encrypt.encrypt_message(message, shift_amount))
elif operation == "decrypt":
    print(decrypt.decrypt_message(message,shift_amount))
else:
    print("invalid operation")
input("Press Enter to exit.")