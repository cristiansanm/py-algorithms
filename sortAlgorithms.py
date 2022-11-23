def bubbleSort(newList):
    aux = 0
    rounds = 0
    isSorted = False

    while (isSorted == False):
        isSorted = True
        for i in range(len(newList) - 1 - rounds):
            if (newList[i] > newList[i + 1]):
                (newList[i+1], newList[i]) = (newList[i], newList[i+1])
                isSorted = False
        rounds = rounds + 1
    print(f'Sorted array {newList}')


bubbleSort([5, 4, 2, 1, 6, 3, 2])


def selectionSort(newList):
    minPos = 0

    for i in range(len(newList)):
        minPos = i
        for j in range(i + 1, len(newList)):
            if (newList[minPos] > newList[j]):
                minPos = j
        (newList[i], newList[minPos]) = (newList[minPos], newList[i])

    print(f'Sorted array by selection {newList}')


selectionSort([5, 4, 2, 1, 6, 3, 2])
