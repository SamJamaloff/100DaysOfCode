# Maze trasure game

side = input("Welcome to Maze treasure\nYour mission is to escape from the maze\nYou are at the gate, you need to make a move\nChoose: L for Left, R for right ").lower()
if side == "l":
    side = input("\n2 hours of walking and you have reached a lake,\nWill you swim to the other side or wait for boat? S for Swim, W for waiting ").lower()
    if side == "s":
        side = input("\nYou have swam well and there are 3 doors. \nOnly one takes you out. Choose one: Red, Green, Yellow ").lower()
        if side == "red":
            print("\nWohooo, you won the game. Congratulations")
        else:
            print("\nYou lost the way, and lost the game")    
    else:
        print("\nYou lost the way, and lost the game")    
else:
    print("You lost the way, and lost the game")