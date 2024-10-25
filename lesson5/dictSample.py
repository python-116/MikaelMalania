person_data = {}

# ask user for personal information and store it in a dictionary

person_data['first_name'] = input("Enter your first name: ")
person_data['last_name'] = input("Enter your last name: ")
person_data['age'] = int(input("Enter your age: "))
person_data['address'] = {}
person_data['address']['street'] = input("Enter your street address: ")

print(person_data)
