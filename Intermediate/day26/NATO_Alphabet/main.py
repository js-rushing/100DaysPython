import pandas
import pyttsx3

# Read NATO Alphabet from csv and create dictionary
nato_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in nato_alphabet.iterrows()}

# Get word from user and create list from NATO Alphabet
user_word = input("Enter a word: ")
user_word_list = [nato_dict[letter.upper()] for letter in user_word]
print(user_word_list)

# Read out the user_word_list using text-to-speech module
talk = pyttsx3.init()
begin = False
for word in user_word_list:
    if not begin:
        talk.say(".")
        talk.say("C Q, C Q, Calling, C Q")
        talk.say(word)
        begin = True
    else:
        talk.say(word)
    talk.runAndWait()
