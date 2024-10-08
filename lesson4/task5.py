try:
    with open("new_file.py", "x") as new_file:
        new_file.write("print('Hello World')")
except FileExistsError:
    print(f"File already exists, please make sure to delete it first")
else:
    print("File created successfully")
finally:
    print("This is the end of the try-except block")
