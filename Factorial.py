num = 0
index = 1
answer = 1

num = int(input("Enter a Number:"))

while (index <= num):
    answer *= index
    index += 1

print("Factorial of",num , "is",answer,".")
