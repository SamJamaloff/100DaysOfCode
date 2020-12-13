# The solution for tipping challenge
total = float(input("What was the total bill? "))
percentage = float(input("What percentage tip would you like to tip? 10, 12, 15 "))
split = float(input("How many people to split th bill? "))

output = round(((total+(total*(percentage/100)))/split), 2)
print(output)
