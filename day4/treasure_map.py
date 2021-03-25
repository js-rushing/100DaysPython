row1 = ["O", "O", "O"]
row2 = ["O", "O", "O"]
row3 = ["O", "O", "O"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

x = input("Where do you want to put the treasure? ")

x_list = x.split(' ')

x_axis = int(x_list[0])
y_axis = int(x_list[1])

map[y_axis-1][x_axis-1] = "X"

print(f"{row1}\n{row2}\n{row3}")
