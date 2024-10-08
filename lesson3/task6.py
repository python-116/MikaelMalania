# *args and **kwargs

def numbers_adder(*numbers):
    sum_of_nums = 0
    # print(type())
    for number in numbers:
        sum_of_nums = sum_of_nums + number

    return sum_of_nums


print(numbers_adder(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
