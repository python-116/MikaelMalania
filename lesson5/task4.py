# using arrays with for loops

person_lived_locations = ['tbilisi', 'batumi', 'kutaisi',
                          'telavi', 'rustavi', 'gurjaani', 'sighnaghi']


# for location in person_lived_locations:
#     print(location)

# using dictionaries with for loops
personList = [["first_name", "John"],
              ["last_name", "Doe"], [
    "age", 30],
    ["hobbies", ["tennis", "football", "swimming"]]]

person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30,
    'hobbies': ['tennis', 'football', 'swimming', 'cycling', 'running', 'dancing', 'singing'],
    'address': {
        'street': '50 Main street',
        'city': 'Boston',
        'state': 'MA'
    }
}

# print(personList[3][1][2])
# print(person.items())

for key, value in person.items():
    # check if fisrt_name is "john" if so
    # then check if his age is greater than 18
    # if so then display his hobbies, use inner if statements
    if key == 'first_name' and value == 'John':
        if person['age'] > 18:
            print("You can vote for the elections.")
