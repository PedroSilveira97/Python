import random
n = random.randint(1, 100)
i = 10
while i > 0:
    guess = int(input("Guess a number between 1 and 100: "))
    if guess != n:
        i = i - 1
    if guess > n:
        print(f"Too high, try again. You have {i} attempts remaining.")
    elif guess < n:
        print(f"Too low, try again. You have {i} attempts remaining.")
    if guess == n:
        print("Congratulations, you got it right.")
        break
if i == 0:
    print("You lose.")
input("Press Enter to exit.")
