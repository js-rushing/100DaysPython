# Mail Merge
#   Read form letter and mailing list from files
#   Format and save personalized letters to output folder


def get_names():
    names_list = []
    with open("./Input/Names/invited_names.txt", mode="r") as names:
        contents = names.readlines()
        for name in contents:
            name = name.replace("\n", "")
            names_list.append(name)
        return names_list


def get_letter():
    with open("./Input/Letters/starting_letter.txt", mode="r") as letter:
        content = letter.read()
        return content


def make_files(mail_list, letter):
    for name in mail_list:
        modified_letter = letter.replace("[name]", f"{name}")
        filename = f"letter_for_{name.replace(' ', '_')}.txt"
        with open(f"./Output/ReadyToSend/{filename}", mode="w") as mail_file:
            mail_file.write(modified_letter)


make_files(get_names(), get_letter())
