def makeArray(messageStr):
    messageArray = []
    for ch in messageStr:
        messageArray.append(ch)
    return messageArray


def getPostShiftIndex(method, preshift, shiftNum):
    if (method == 'encode'):
        newIndex = preshift + shiftNum
        if (newIndex > 25):
            newIndex -= 26
    else:
        newIndex = preshift - shiftNum
        if (newIndex < 0):
            newIndex += 26
    return newIndex


def caesar(programMode, letterArr, messageStr, shiftNum):
    messageArray = makeArray(messageStr)
    encodedArray = []
    count = 0
    for ch in messageArray:
        count += 1
        if (ch in letterArr):
            preShiftIndex = letterArr.index(ch)
            postShiftIndex = getPostShiftIndex(
                programMode, preShiftIndex, shiftNum)
            encodedArray.append(letterArr[postShiftIndex])
        else:
            encodedArray.append(ch)
    encodedString = ''.join(encodedArray)
    return encodedString
