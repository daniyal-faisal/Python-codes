index = 1 
prev = 0
nex = 1
terms = 0
temp = 0

terms = int(input("Enter number of Terms:"))

print(prev)

while(index < terms):
    print(nex)
    temp = nex
    nex = prev + nex
    prev = temp
    index += 1
