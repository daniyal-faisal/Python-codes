def factorial(num):
    index = 1
    answer = 1

    while (index <= num):

        answer *= index
        index += 1

    return answer


n = 0
r= 0
n = int(input("Enter a value for n:"))
r = int(input("Enter a value for r:"))

if(r > n or r < 0 or n <= 0):
    print("ERROR")
else:
    print("nCr is",factorial(n)/(factorial(n-r)*factorial(r)))
