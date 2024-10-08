with open('./files/texts/info.txt', 'r+') as info_file:
    data = info_file.read()
    print(data)
    info_file.write('\nThis is some new data')

# with open('./files/texts/info.txt') as info_file:
#     data = info_file.read()
#     print(data)
    # data.write('This is some new data')
