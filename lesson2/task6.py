# break and continue statements in while loop

count = 0

while count < 10:
    count = count + 1
    if count % 2 == 0:
        continue
    print(f"Count is {count}")

print("=====================================")


count2 = 0

while count2 < 10:
    count2 = count2 + 1
    if count2 == 5:
        break
    print(f"Count is {count2}")
