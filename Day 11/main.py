import random

import new_card

cards_values = {"A": 11, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
                "8": 8, "9": 9, "10": 10, "j": 10, "q": 10, "k": 10}

# Player's Draw
value = 0
cards_values_list = list(cards_values.values())
random.shuffle(cards_values_list)
players_cards = cards_values_list[:2]
for i in range(len(players_cards)):
    value = value + players_cards[i]
print(f"Your cards values are {players_cards}, and your points are {value}. ")

# PC's Draw
value_pc = 0
cards_values_list = list(cards_values.values())
random.shuffle(cards_values_list)
pc_cards = cards_values_list[:2]
for i in range(len(pc_cards)):
    value_pc = value_pc + pc_cards[i]
for card in pc_cards:
    if value_pc > 16:
        if card == 11:
            q_pc = "yes"
        else:
            q_pc = "no"
    else:
        q_pc = "yes"

# reset
cards_values_list = list(cards_values.values())

# Player's Turn
q_player = str(input("Would you like to draw? "))
while new_card.new_card_function(q_player):
    players_cards.append(random.choice(cards_values_list))
    value = 0
    for i in range(len(players_cards)):
        value = value + players_cards[i]
    for card in players_cards:
        if card == 11:
            if value > 21:
                value = value - 10
    print(f"Your cards are {players_cards}, and your points are now {value}. ")
    if value > 21:
        break
    q_player = str(input("Would you like to draw? "))

# PC's turn
while new_card.new_card_function(q_pc):
    pc_cards.append(random.choice(cards_values_list))
    value_pc = 0
    for i in range(len(pc_cards)):
        value_pc = value_pc + pc_cards[i]
    for card in pc_cards:
        if card == 11:
            if value > 21:
                value_pc = value_pc - 10
        if value_pc > 16:
            if card == 11:
                q_pc = "yes"
            else:
                q_pc = "no"
        else:
            q_pc = "yes"

    print(f"The PC cards are {pc_cards}, and their points are now {value_pc}. ")
    if value_pc > 21:
        break

if value_pc > 21:
    if value > 21:
        print(f"Your cards are {players_cards}. Your score is {value}")
        print(f"The pc's cards are {pc_cards}. Their score is {value_pc}")
        print("You and the pc busted. It's a tie. ")
    else:
        print(f"Your cards are {players_cards}. Your score is {value}")
        print(f"The pc's cards are {pc_cards}. Their score is {value_pc}")
        print("The pc busted. You win. ")
elif value > 21:
    if value_pc > 21:
        print(f"Your cards are {players_cards}. Your score is {value}")
        print(f"The pc's cards are {pc_cards}. Their score is {value_pc}")
        print("You and the pc busted. It's a tie. ")
    else:
        print(f"Your cards are {players_cards}. Your score is {value}")
        print(f"The pc's cards are {pc_cards}. Their score is {value_pc}")
        print("You busted. You lose. ")
elif value > value_pc:
    print(f"Your cards are {players_cards}. Your score is {value}")
    print(f"The pc's cards are {pc_cards}. Their score is {value_pc}")
    print("You win. ")
elif value_pc > value:
    print(f"Your cards are {players_cards}. Your score is {value}")
    print(f"The pc's cards are {pc_cards}. Their score is {value_pc}")
    print("You lose. ")
elif value == value_pc:
    print(f"Your cards are {players_cards}. Your score is {value}")
    print(f"The pc's cards are {pc_cards}. Their score is {value_pc}")
    print("It's a tie. ")

input("Press Enter to exit")
