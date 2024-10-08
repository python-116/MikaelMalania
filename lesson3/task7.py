# **kwargs example

def students(**studentData):
    print(studentData)
    for key, value in studentData.items():
        print(f'{key}: {value}')


students(name='John', age=25, course='Python')
students(name='Jack', age=30, course='Java')
