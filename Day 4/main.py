import random
player_choice = str(input("What do you choose?\nRock\nPaper\nScissors"))
computer_options = ["Rock", "Paper", "Scissors"]
player_choice = player_choice.lower()
computer_choice = random.randint(0, len(computer_options)-1)
print(f"The computer chose {computer_options[computer_choice]}")
if player_choice == "rock":
    if computer_choice == 0:
        print("It's a tie.")
    elif computer_choice == 1:
        print("You lose.")
    else:
        print("You win.")
elif player_choice == "paper":
    if computer_choice == 0:
        print("You win.")
    elif computer_choice == 1:
        print("It's a tie.")
    else:
        print("You lose.")
elif player_choice == "scissors":
    if computer_choice == 0:
        print("You lose.")
    elif computer_choice == 1:
        print("You win.")
    else:
        print("it's a tie.")
