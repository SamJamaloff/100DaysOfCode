# bankers roulette game script

import random
names = input("Give me name, seperated by a comma. ").split(", ")

#this is the one way
name = names[random.randint(0, len(names) - 1)]
print(f"{name} is going pay for today")

#this is the second way 
name = random.choice(names)
print(f"{name} is going pay for today")
