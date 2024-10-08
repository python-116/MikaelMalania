# with open("./files/texts/info.txt", "r") as data_file:
#     print(data_file.read())

# with open("./files/texts/info.txt", "w") as data_file:
#     data_file.write("Lorem Lorem Ipsum Ipsum!")

with open("./files/texts/info.txt", "a") as data_file:
    data_file.write('\nsome other data')
    data_file.write('\nsome newer data')
