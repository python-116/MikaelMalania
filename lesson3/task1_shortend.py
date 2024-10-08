def compare_numbers(num1, num2):
    if num1 > num2:
        return 'num1 is greater than num2'
    elif num1 < num2:
        return 'num1 is less than num2'
    else:
        return 'num1 is equal to num2'


print(compare_numbers(30, 20))
print(compare_numbers(20, 30))
print(compare_numbers(20, 20))
print(compare_numbers(10, 15))
