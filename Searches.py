def linearSearch(UI, lst):
    for x in range(len(lst)):
        if UI == lst[x]:
            return 1
        else:
            return 0



def binarySearch(UI,lst):
    UB = len(lst)
    LB = 1
    isFound = False
    notinList = False
    try:
        while isFound == False and notinList == False:
            mid = int((UB + LB) / 2)
            if lst[mid] == UI:
                isFound = True
                return 1
            else:
                if lst[mid] > UI:
                    UB = mid - 1
                else:
                    LB = mid + 1
            if LB > UB:
                notinList = True
                return 1
    except IndexError:
            return 0


# Main
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]



Selection = int(input('''Please Select from the following:
    1 - Linear Search
    2 - Binary Search
    0 - Exit
Selection:'''))



CD = False


while Selection != 0 :

    if Selection == 1:
        UI = int(input("Enter a number to be searched:"))
        replyLS = linearSearch(UI,lst)
        if replyLS == 1:
            print('Your number is Found')
            CD = True
        else:
            if replyLS == 0:
                print('Your number is NOTFound')
                CD = True
    elif Selection == 2:
            UI = int(input("Enter a number to be searched:"))
            replyBS = binarySearch(UI, lst)
            if replyBS == 1:
                print('Your number is Found')
                CD = True
            else:
                if replyBS == 0:
                    print('Your number is NOTFound')
                    CD = True
    print("Please select from menu only!!!")
    Selection = int(input('''Please Select from the following:
        1 - Linear Search
        2 - Binary Search
Selection:'''))






