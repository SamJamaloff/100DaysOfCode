# checking for height and age 


height = int(input("What is you height? "))

if height > 120 :
    print("You are welcome!!! ")
    age = int(input("What is your age? "))
    if age < 12:
        print("Please pay $5")
    elif age <=18:
        print("Please pay $7")
    else:
        print("Please pay $12")
else: 
    print("Come back when grow!!!")