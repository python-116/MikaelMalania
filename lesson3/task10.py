# yeild functions in python

def simple_easy_generator():
    yield "1"
    yield "hello"
    yield "there"


generator = simple_easy_generator()

myArr = ['james', 'john', 'bob', 'bill', 'jane']

myArr = iter(myArr)

print(next(generator))
print(next(generator))
print(next(generator))


# for value in generator:
#     print(value)
