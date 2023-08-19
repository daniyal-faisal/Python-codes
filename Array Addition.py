Sum = 0
index = 0
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

arraysize = len(numbers)
print("Array Size:",arraysize)

while (index < arraysize):
    Sum = Sum + numbers[index]
    index += 1
    
print("Sum:",Sum)
