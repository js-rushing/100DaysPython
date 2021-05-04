numbers = [1, 2, 3]

# new_list = []
# for n in numbers:
#     add_1 = n + 1
#     new_list.append(add_1)
# print(new_list)

# LIST COMPREHENSION
#   The functionality of the above code in one line
# new_list = [n + 1 for n in numbers]
# print(new_list)
#
# name = "Angela"
# name_list = [letter for letter in name]
# print(name_list)
#
# range_list = [n * 2 for n in range(1, 5)]
# print(range_list)
#
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# short_names = [name for name in names if len(name) < 5]
# print(names)
# print(short_names)
# long_names = [name.upper() for name in names if len(name) >= 5]
# print(long_names)

# SQUARING NUMBERS CHALLENGE
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_numbers = [n**2 for n in numbers]
# print(squared_numbers)

# FILTERING EVEN NUMBERS CHALLENGE
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# result = [n for n in numbers if n % 2 == 0]
# print(result)

# DATA OVERLAP CHALLENGE
with open("file1.txt") as file1:
    list1 = file1.readlines()
with open("file2.txt") as file2:
    list2 = file2.readlines()
result = [int(n) for n in list1 if n in list2]
print(result)
