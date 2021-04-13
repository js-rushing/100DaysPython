student_heights = input("Input a list of student heights ").split(' ')
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

total = 0

for height in student_heights:
    total += height

avg = int(total / len(student_heights))

print(f"The average height is {avg}.")

# 156 178 165 171 187
