# pizza delivery coding challenge

size = input("Welcome to pizza Deliveries!\nWhat size of Pizza do you want S, M, L ? ")
pepperoni = input("Do you want some pepperoni? Y/N ")
cheese = input("How about extra cheese? Y/N ")

bill = 0
if size == "S":
    bill += 15  
    if pepperoni == "Y":
        bill += 2      
elif size == "M":
    bill += 20
    if pepperoni == "Y":
        bill += 3
elif size == "L":
    bill += 25
    if pepperoni == "Y":
        bill += 3


if cheese == "Y":
    bill += 1

print(f"Totall: ${bill}")