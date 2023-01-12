global filename
filename = "def.txt"
Array = []

def readdata(Array):
    try:
        global filename
        file = open(filename, "r")
        desc = (file.readline()).strip()
        while desc != "":
            wdt = (file.readline()).strip()
            hgt = (file.readline()).strip()
            fclr = (file.readline()).strip()

            Array.append(desc)
            Array.append(wdt)
            Array.append(hgt)
            Array.append(fclr)

            desc = (file.readline()).strip()
        file.close()
    except IOError:
        print("file NOT Found")
    return Array
# Main
reply = readdata(Array)
if reply !=[]:
    print(reply)

