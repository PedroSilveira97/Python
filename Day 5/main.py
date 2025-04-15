import random
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
            "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
UC_alphabet = []
for letter in alphabet:
    UC_alphabet.append(letter.upper())
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
special = ["!", "@", ".", "_", "?", "$"]
password = ""
password_list = []
number_lc = int(input("How many lowercase letters do you want in your password?"))
number_up = int(input("How many uppercase letters do you want in your password?"))
number_numbers = int(input("How many numbers do you want in your password?"))
number_special = int(input("How many special characters do you want in your password?"))
for char in range(1, number_lc + 1):
    password_list.append(random.choice(alphabet))
for char in range(1, number_up + 1):
    password_list.append((random.choice(UC_alphabet)))
for char in range(1, number_numbers + 1):
    password_list.append((random.choice(numbers)))
for char in range(1, number_special + 1):
    password_list.append((random.choice(special)))
random.shuffle(password_list)
for char in password_list:
    password = password + char
print(f"Your password is {password}")