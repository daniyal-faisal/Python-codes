nLst = []


def createList():
    global nLst
    noE = int(input("How many elements do you need in the list? : "))
    for x in range(1, ((noE) + 1)):
        print("Element", x)
        E = int(input("=>"))
        nLst.append(E)
    print(nLst)


def bubbleSort():
    global nLst
    bouandary = len(nLst) - 1
    noSwaps = False
    while not noSwaps:
        noSwaps = True
        for j in range(bouandary):
            if nLst[j] > nLst[j + 1]:
                temp = nLst[j]
                nLst[j] = nLst[j + 1]
                nLst[j + 1] = temp
                noSwaps = False
        bouandary = bouandary - 1
    if nLst == []:
        print('PLEASE CREATE A LIST')
    else:
        print(nLst)


def insersionSort():
    global nLst
    for j in range(1, len(nLst)):
        temp = nLst[j]
        cpt = j
        while cpt > 0 and nLst[cpt - 1] > temp:
            nLst[cpt] = nLst[cpt - 1]
            cpt -= 1
        nLst[cpt] = temp
    if nLst == []:
        print('PLEASE CREATE A LIST')
    else:
        print(nLst)
    #print(nLst)


# Main
Selection = int(
    input(
        """Please Select from the following:
    1 - Create List
    2 - Bubble Sort
    3 - Insersion Sort
    0 - Exit
Selection:"""
    )
)
while Selection != 0 :
    if Selection == 1:
        createList()
    elif Selection == 2:
        bubbleSort()
    elif Selection == 3:
        insersionSort()
    Selection = int(
        input(
            """Please Select from the following:
        1 - Create List
        2 - Bubble Sort
        3 - Insersion Sort
        0 - Exit
    Selection:"""
        )
    )
