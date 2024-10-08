with open('new_file.txt', 'wb') as new_file:
    data = bytearray([0x2, 0x25, 3, 4, 5])
    new_file.write(data)
