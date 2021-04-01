student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62
}
# Don't change the code above

# Todo-1: Create an empty dictionary called student_grades.
student_grades = {}

# Todo-2: Write your code below to add the grades to student_grades.
for key in student_scores:
    if student_scores[key] > 90 and student_scores[key] <= 100:
        student_grades[key] = 'Outstanding'
    elif student_scores[key] > 80 and student_scores[key] <= 90:
        student_grades[key] = 'Exceeds Expectations'
    elif student_scores[key] > 70 and student_scores[key] <= 80:
        student_grades[key] = 'Acceptable'
    else:
        student_grades[key] = 'Failing'

# Don't change the code below
print(student_grades)
