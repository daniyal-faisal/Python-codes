'''
Q1
'''

TheData = [20, 3, 4, 8, 12, 99, 4, 26, 4]


def InsersionSort(TheData):
    for count in range(1, len(TheData) - 1):
        DataToInsert = TheData[count]
        Inserted = 0
        NextValue = count - 1
        while NextValue >= 0 and Inserted != 1:
            if DataToInsert < TheData[NextValue]:
                TheData[NextValue + 1] = TheData[NextValue]
                NextValue = NextValue - 1
                TheData[NextValue + 1] = DataToInsert
            else:
                Inserted = 1
    return TheData


def outputAll(TheData):
    for i in range(len(TheData)):
        print(TheData[i])


def checkElement(DTC, TheData):
    for j in range(len(TheData)):
        if DTC == TheData[j]:
            return True
    return False


# Main
print("Array Before Sorting")
outputAll(TheData)
print("Array After Sorting")
print(InsersionSort(TheData))
DTC = int(input("Enter an element to check: "))
reply = checkElement(DTC, TheData)
if reply == True:
    print("found")
else:
    print("not found")
