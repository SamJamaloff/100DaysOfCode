#Password Generator Project

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))
ch_letters = ""
for i in range(0, nr_letters):
    ch_letters += random.choice(letters)
ch_numbers = ""
for i in range(0, nr_numbers):
    ch_numbers += random.choice(numbers)
ch_symbols = ""
for i in range(0, nr_symbols):
    ch_symbols += random.choice(symbols)
final_answer = ch_letters + ch_numbers + ch_symbols
print(f"This is the easy version: --> {final_answer}")
temp = list(final_answer)
random.shuffle(temp)
final_answer = ""
for i in temp:
    final_answer += i
print(f"This is the hard version: --> {final_answer}")