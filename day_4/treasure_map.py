# this is a code for treasure map coding challenge
row1 = ['⬜️', '⬜️', '⬜️']
row2 = ['⬜️', '⬜️', '⬜️']
row3 = ['⬜️', '⬜️', '⬜️']
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
d1, d2 = int(position[0])-1, int(position[1])-1
map[d2][d1] = "X"
print(f"{row1}\n{row2}\n{row3}")
