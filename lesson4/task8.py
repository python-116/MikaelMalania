def number_divisor(number):
    try:
        number = int(number)
        result = 10 / number
    except ZeroDivisionError as e:
        print("Division by zero is not allowed")
    except ValueError as e:
        print("Only numbers are allowed")
    except Exception as e:
        print(f"An error occured: {e}")
    else:
        print(f"Result is {result}")
    finally:
        print("This is the end of the function")


user_input = input("Enter a number: ")

number_divisor(user_input)
