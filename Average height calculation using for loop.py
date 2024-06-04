# A program that calculates the average height of students

student_heights = input("Enter the heights here, separate with commas\n").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights) 

# calculating te sum
total_height = 0
for height in student_heights:
    total_height = total_height + height

# calculating the number of people
number_of_people = 0
for person in student_heights:
    number_of_people = number_of_people + 1
    
# calculating the average
average = round(total_height / number_of_people)

print(f"The average height is {average}")
