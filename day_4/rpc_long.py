
import random
import game_images
user_choice = int(input("1 -> Rock, 2 -> Paper, 3 -> Scissors "))

actions = [game_images.rock, game_images.paper, game_images.scissors]
comp_choice = random.randint(1, 3)

if user_choice == 1:
    if comp_choice == 1:
        print(f"Your choice rock {actions[user_choice-1]}\ncomputer's choice rock {actions[comp_choice-1]}\nDRAW.")
    elif comp_choice == 2:
        print(f"Your choice rock {actions[user_choice-1]}\ncomputer's choice paper {actions[comp_choice-1]}\nyou lose")
    else:
        print(f"Your choice rock {actions[user_choice-1]}\ncomputer's choice scissors {actions[comp_choice-1]}\nYOU WON!!!")

elif user_choice == 2:
    if comp_choice == 1:
        print(f"Your choice paper {actions[user_choice-1]}\ncomputer's choice rock {actions[comp_choice-1]}\nYOU WON!!!")
    elif comp_choice == 2:
        print(f"Your choice paper {actions[user_choice-1]}\ncomputer's choice paper {actions[comp_choice-1]}\nDRAW")
    else:
        print(f"Your choice paper {actions[user_choice-1]}\ncomputer's choice scissors {actions[comp_choice-1]}\nyou lose!!!")                

elif user_choice == 3:
    if comp_choice == 1:
        print(f"Your choice scissors {actions[user_choice-1]}\ncomputer's choice rock {actions[comp_choice-1]}\nyou lose.")
    elif comp_choice == 2:
        print(f"Your choice scissors {actions[user_choice-1]}\ncomputer's choice paper {actions[comp_choice-1]}\nYOU WON!!!")
    else:
        print(f"Your choice scissors {actions[user_choice-1]}\ncomputer's choice scissors {actions[comp_choice-1]}\nDRAW")
