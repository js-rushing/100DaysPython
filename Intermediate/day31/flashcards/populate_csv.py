import json
import pandas

with open("data/german_english.json") as file:
    word_dict = json.load(file)

german_list = []
english_list = []

for word in word_dict.keys():
    german_list.append(word)
    english_list.append(word_dict[word])

german_english_dict = {
    "German": german_list,
    "English": english_list
}

data_frame = pandas.DataFrame(german_english_dict)

data_frame.to_csv("./data/german_english.csv", index=False)
