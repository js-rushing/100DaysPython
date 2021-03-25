student_scores = input("Input a list of student heights ").split(' ')
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

# maximum = max(student_scores)
maximum = 0

for score in student_scores:
    current = score
    if (current > maximum):
        maximum = score

print(f"The highest score in the class is: {maximum}")


# 78 65 89 86 55 91 64 89
