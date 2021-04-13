from cipher_functions import makeArray
from cipher_functions import getPostShiftIndex
from cipher_functions import caesar
from cipher_reference import letterArr


goAgain = True

while (goAgain):
    programMode = input(
        'Type \'encode\' to encrypt, type \'decode\' to decrypt: \n')

    message = input('Type your message: \n').lower()
    shiftNum = int(input('Type the shift number: \n'))
    if (shiftNum > 26):
        while (shiftNum > 26):
            shiftNum -= 26

    result = caesar(programMode, letterArr, message, shiftNum)

    print(f"Here's the {programMode}d result: {result}")
    if (input("Type 'yes' if you want to go again.  Otherwise type anything else.").lower() != 'yes'):
        goAgain = False
