global filename
filename = "Alpha.txt"
Array = []

def readdata(Array):
    try:
        global filename
        file = open(filename, "r")
        DF = (file.readline()).strip()
        while DF != "":
            Array.append(DF)
            DF = (file.readline()).strip()
        file.close()
    except IOError:
        print("file NOT Found")
    return Array

def adddata():
    DTA = input(str("add an element to Add to array:"))
    Array.append(DTA)


# Main
reply = readdata(Array)

Selection = int(input('''Choose from the following:
    1 - Display Array
    2 - Add Data
    0 - Exit
Selection:'''))
while Selection != 0:

    if Selection == 1:

        if reply !=[]:
            print(reply)
    elif Selection == 2:
        adddata()
    Selection = int(input('''Choose from the following:
    1 - Display Array
    2 - Add Data
    0 - Exit
Selection:'''))
