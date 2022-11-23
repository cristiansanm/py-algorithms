print("arrays!")

myList = ["apple", "banana", "cherry", "pinneapple"]

for i in range(len(myList)):
    print(f'Value: {myList[i]}, position: {i}')


def addElementsToList():
    listLength = input('Enter the list length:\n')
    myNewList = []
    for i in range(int(listLength)):
        value = input('Insert a value \n')
        myNewList.append(value)
    print(myNewList)


addElementsToList()


def checkPal(word: str):
    sameChar = True
    for i in range(round(len(word)/2)):
        lastPosition = len(word) - 1 - i
        print(word[lastPosition])
        if (word[i] != word[lastPosition]):
            sameChar = False
    print(f'The word {word} is {"" if sameChar else "not"} pal')


checkPal('acrissirca')


def calculateMinorGreatterAndMedia(list):
    maxValue = 0
    minValue = list[0]
    media = 0
    for x in list:
        media += x
        if (maxValue < x):
            maxValue = x
        else:
            if maxValue >= minValue and minValue > x:
                minValue = x
    print(
        f'Max number {maxValue}, min number {minValue}, media {round(media/len(list))}')


calculateMinorGreatterAndMedia([-0.23, 2.45, 3.65, 4.76, 9.43, 7.23, 242.40])
