# calculating lovers score
print("Welcom to Love calculator")
name_1 = input("1st name: ").lower()
name_2 = input("2nd name: ").lower()

first_digit = 0
second_digit = 0

first_digit += name_1.count("t")
first_digit += name_1.count("r")
first_digit += name_1.count("u")
first_digit += name_1.count("e")
second_digit += name_1.count("l")
second_digit += name_1.count("o")
second_digit += name_1.count("v")
second_digit += name_1.count("e")

first_digit += name_1.count("t")
first_digit += name_1.count("r")
first_digit += name_1.count("u")
first_digit += name_1.count("e")
second_digit += name_1.count("l")
second_digit += name_1.count("o")
second_digit += name_1.count("v")
second_digit += name_1.count("e")

love_score = int(str(first_digit) + str(second_digit))

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together coke and menthos")
elif 40 < love_score < 50:
    print(f"Your score is {love_score}, you are alright together")
else:
    print(f"Your score is {love_score}")

