# tossing coing using random function
import random 

# 1 for heads 
# 0 for tails

random_side = random.randint(0, 1)

if random_side == 1:
    print("Heads")
else:
    print("Tails")