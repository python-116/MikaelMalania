# notes application
user_input = input(
    "Enter Action (create, read, update, delete, exit): ").lower()

if user_input == 'create':
    # digital education
    note_title = input("Enter note title: ")
    # learning about python programming
    note_content = input("Enter note content: ")
    with open(note_title+'.txt', 'x') as note_file:
        note_file.write(note_content)
# elif user_input == 'read':
# elif user_input == 'update':
# elif user_input == 'delete':
# elif user_input == 'exit':
