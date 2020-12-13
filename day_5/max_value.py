# this is max_value.py file and in here max value of students is calculated

student_scores = input("Input a list of students scores ").split()

for i in range(0, len(student_scores)):
    student_scores[i] = int(student_scores[i])

max_value = 0
for score in student_scores:
    if score > max_value:
        max_value = score
print(f"The highest score in the class is: {max_value}")