# this is a script for calculating the average height of students of 
student_heights = input("Input a list of students height ").split()
for i in range(0, len(student_heights)):
    student_heights[i] = int(student_heights[i])

count = 0
temp_height = 0
for height in student_heights:
    count += 1
    temp_height += height

average = temp_height//count
print(average)