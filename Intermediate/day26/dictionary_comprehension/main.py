# DICTIONARY COMPREHENSION
# from random import randint

# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# students_scores = {student: randint(55, 100) for student in names}
# print(students_scores)
#
# passed_students = {student: score for (student, score) in students_scores.items() if score >= 70}
#
# print(passed_students)

# DICTIONARY COMPREHENSION CHALLENGE 1
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word: len(word) for word in sentence.split()}
print(result)

# DICTIONARY COMPREHENSION CHALLENGE 2
# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24
# }
# weather_f = {day: int(temp * 9/5 + 32) for (day, temp) in weather_c.items()}
# print(weather_f)
