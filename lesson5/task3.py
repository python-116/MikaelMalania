import json
# dictionaries in python
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30,
    'hobbies': ['tennis', 'football', 'swimming', 'cycling', 'running', 'dancing', 'singing'],
    'address': {
        'street': '50 Main street',
        'city': 'Boston',
        'state': 'MA',
        'family_members': {
            'father': 'George',
            'mother': 'Kate',
            'children': ['Mike', 'Sophia']
        }
    }
}

student = {
    "first_name": "Jane",
    "last_name": "Smith",
    "age": 25,
    "hobbies": ["painting", "cooking", "gardening"],
    "address": {
        "street": "123 Elm Street",
        "city": "Los Angeles",
        "state": "CA"
    }
}

# Pop item from dictionary

# person['address'].pop('street')
# print(json.dumps(person, indent=2))

# # Pop last item from dictionary
# person.popitem()
# person.popitem()

# print(person)

# # Add item to dictionary
person['phone'] = '555-555-5555'

print(json.dumps(person, indent=2))
