from playsound import playsound
import time

# Get text to be converted from user
text = input('Enter text to be converted to Morse code:').lower()

# Time Units Constants
# Space between dots/dashes in same letter  = 1 time unit
# Space between letters                     = 3 time units
# Space between words                       = 7 time units
time_unit = .03
between_letters = 3 * time_unit
between_words = 7 * time_unit


# Create object where key is character and value is equivalent morse code string
morse_dict = {
    'a': '.-',
    'b': '-...',
    'c': '-.-.',
    'd': '-..',
    'e': '.',
    'f': '..-.',
    'g': '--.',
    'h': '....',
    'i': '..',
    'j': '.---',
    'k': '-.-',
    'l': '.-..',
    'm': '--',
    'n': '-.',
    'o': '---',
    'p': '.--.',
    'q': '--.-',
    'r': '.-.',
    's': '...',
    't': '-',
    'u': '..-',
    'v': '...-',
    'w': '.--',
    'x': '-..-',
    'y': '-.--',
    'z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '10': '-----',
    ' ': ' ',
}


# Function, takes a string and returns list of characters in string
def split_str(s):
    return [ch for ch in s]


# Split text into list of characters
text_list = split_str(text)

# Iterate through list and push converted morse strings into new list
morse_list = [morse_dict[ch] for ch in text_list]

# Join that list into new string
morse_str = ' '.join(morse_list)

# Print new string to console
print(morse_str)


# Play audio of morse code by iterating through list
for letter in morse_list:
    # Iterate through all characters in letter
    for j in range(len(letter)):
        ch = letter[j]
        last_char = False
        # If char is last in letter
        if j == len(letter) - 1:
            last_char = True

        # If between words
        if ch == ' ':
            time.sleep(between_words)
        else:
            if ch == '.':
                playsound('dot.mp3')
            elif ch == '-':
                playsound('dash.mp3')
            time.sleep(time_unit)
            # If between letters
            if last_char:
                time.sleep(between_letters)
