import pandas

fur_color_dict = {
    "Fur Color": ["gray", "red", "black"],
    "Count": [0, 0, 0]
}

squirrel_data = pandas.read_csv("Squirrel_Data.csv")
fur_color_list = squirrel_data["Primary Fur Color"].to_list()
for color in fur_color_list:
    if color == "Gray":
        fur_color_dict["Count"][0] += 1
    elif color == "Cinnamon":
        fur_color_dict["Count"][1] += 1
    elif color == "Black":
        fur_color_dict["Count"][2] += 1

data_frame = pandas.DataFrame(fur_color_dict)

data_frame.to_csv("squirrel_count.csv")

