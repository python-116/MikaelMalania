# functions optional arguments

def calculate(a, b, operation="add"):
    if operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b
    elif operation == 'multiply':
        return a * b
    elif operation == 'divide':
        return a / b
    else:
        print("I don't know that one")


print(calculate(4, 5))
print(calculate(4, 5, 'subtract'))
