# simple calculator with function

def calculator(num1, num2, eq):
    if eq == '+':
        return 'result', num1 + num2
    elif eq == '-':
        return num1 - num2
    elif eq == '*':
        return num1 * num2
    elif eq == '/':
        return num1 / num2
    else:
        print('Invalid operator')


# num1 = int(input('Enter first number: '))
# eq = input('Enter operator: ')
# num2 = int(input('Enter second number: '))

# print(calculator(num1, num2, eq))

# calculator void variant with print


def calculator_void(num1, num2, eq):
    if eq == '+':
        print('Result:', num1 + num2)
    elif eq == '-':
        print('Result:', num1 - num2)
    elif eq == '*':
        print('Result:', num1 * num2)
    elif eq == '/':
        if num2 != 0:
            print('Result:', num1 / num2)
        else:
            print('Error: Division by zero')


calculator_void(45, 34, "-")+5
