# Number checker with nested if statements

num = int(input("Enter a number: "))

if num > 0:
    print("Number is positive")
else:
    if num < 0:
        print("Number is negative")
    else:
        print("Number is zero")
