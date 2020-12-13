#rock is 1  #paper is 2  #scissors is 3
import random
import game_images
user_choice = int(input("1 -> Rock, 2 -> Paper, 3 -> Scissors "))
if 1 <= user_choice <=3:
    actions = [game_images.rock, game_images.paper, game_images.scissors]
    comp_choice = random.randint(1, 3)
    row1, row2, row3 = ["Draw", "Win", "Lose"], ["Lose", "Draw", "Win"], ["win", "Lose", "Draw"]
    mapping = [row1, row2, row3]
    d1, d2 = comp_choice-1, int(user_choice)-1
    decision = mapping[d1][d2] 
    print(f"Your choice{actions[d2]}\nComputer's choice{actions[d1]}\n\n{decision}\n\n")
else:
    print("You made wrong choice. You lose!!!")