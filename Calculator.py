num1 = 0 
num2 = 0
opp = ''

num1 = int(input("Enter first number:"))
opp = input("Enter a operator:")
num2 = int(input("Enter second number:"))


if opp == '+':
    print( num1 + num2)
elif opp == '-':
    print(num1 - num2)
elif opp == '*':
    print(num1 * num2)
elif opp == '/':
    print(num1 / num2)
else:
    print("wrong operator")

