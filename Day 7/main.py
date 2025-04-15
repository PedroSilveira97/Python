import getpass
word = getpass.getpass("Choose the word for this game").lower()
wrong_list = []
right_list = ["_"] * len(word)
attempt = 0
while attempt < 6:
    right = ""
    wrong = ""
    guess = str(input("What is your guess")).lower()
    if guess in word:
        i = word.index(guess)
        right_list[i] = guess
    else:
        wrong_list.append(guess)
        attempt = attempt + 1
    for char in wrong_list:
        wrong = wrong + char
    for char in right_list:
        right = right + char
    print(f"Wrong letters: {wrong}. \nWord: {right}")
    if attempt == 6:
        print("You didn't guess the word correctly")
    if right == word:
        print("Congratulations, you guessed it!")
        break
