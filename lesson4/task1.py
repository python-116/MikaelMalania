def divide(x, y):
    try:
        result = x / y
    except Exception as error:
        print("An error occurred: ", error)
        # print("Division by zero is not allowed.")
        result = None
    else:
        print("Division operation complete.")
    finally:
        return result


print(divide(10, 2))
print(divide(10, 0))
print(divide(10, 5))
