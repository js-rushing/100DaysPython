# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

# SAME FUNCTIONALITY

# closes automatically
# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# mode "w" for write
# with open("my_file.txt", mode="w") as file:
#     file.write("New text.")

# mode "a" for append
# with open("my_file.txt", mode="a") as file:
#     file.write("\nNew text.")

# if file doesn't exist it gets created
with open("../../../../../Desktop/new_file.txt", mode="a") as file:
    file.write("\n\nSome new text.")
