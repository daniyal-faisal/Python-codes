'''
Q2
'''

class HiddenBox:
    # __BoxName String
    # __Creator String
    # __DateHidden String
    # __GameLocation String
    # __LastFinds [10][2] String
    # __Active String

    def __init__(self, BXN, CRE, DH, GL):
        self.__BoxName = BXN
        self.__Creator = CRE
        self.__DateHidden = DH
        self.__GameLocation = GL
        self.__LastFinds = [["" for j in range(0, 2)] for i in range(0 ,10)]
        self.__Active = False
    def GetBoxName():
        return self.__BoxName
    def GetGameLocation():
        return self.__GameLocation

def NewBox(TheBoxes, NumBoxes):
    Name = str(input("Input Name: "))
    Creator = str(input("Input Creator: "))
    DateHidden = str(input("Input Date Hidden: "))
    GameLocation = str(input("Input GameLocation: "))
    TheBoxes[NumBoxes] = HiddenBox(Name, Creator, DateHidden, GameLocation)
    return(NumBoxes + 1)
class PuzzleBox(HiddenBox):
    # PT String
    # SL String
    def __init__(self, BXN, CRE, DH, GL, PT, SL):
        super().__init__(BXN, CRE, DH, GL)
        self.__PuzzleText = PT
        self.__Solution = SL
# Main
NumBoxes = 0
TheBoxes = [HiddenBox("", "", "", "")for i in range(1, 10000)]
NumBoxes = NewBox(TheBoxes, NumBoxes)


