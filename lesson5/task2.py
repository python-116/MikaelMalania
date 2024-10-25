person_hobbies = ['tennis', 'football', 'swimming',
                  'cycling', 'running', 'dancing', 'singing']

# 1. Append to the list
person_hobbies.append('reading')
# append() adds an item to the end of the list
person_hobbies.append('writing')
# print(person_hobbies)

# 2. Pop from the list
person_hobbies.pop(2)

print(person_hobbies)

# 3. Remove item by item value
person_hobbies.remove('running')

print(person_hobbies)

# 4. Insert item at a specific index
person_hobbies.insert(2, 'astronomy')

print(person_hobbies)

# 5. Calculate the length of the list
list_length = len(person_hobbies)
print(person_hobbies[list_length - 1])

# 6. count() method
print(person_hobbies.count('dancing'))

# 7. sort() method
person_hobbies.sort(reverse=True)

# 8. reverse() method
person_hobbies.reverse()

# 9. min() method
print(min(person_hobbies))

# 10. max() method
print(max(person_hobbies))

# 11. index() method
print(person_hobbies.index('tennis'))

# 12. copy() method
person_hobbies_copy = person_hobbies.copy()

# 13. sum() method
numbers = [1, 2, 3, 4, 5]
print(sum(numbers))
