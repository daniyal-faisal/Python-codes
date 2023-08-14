Year = 0
Year = int(input("Enter a year:"))

if(Year%4 == 0 and Year%100 != 0):
    print(Year,"is a Leap Year.")
else:
    print(Year,"is not a Leap Year.")
