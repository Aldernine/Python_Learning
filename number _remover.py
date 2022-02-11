numbers = [2, 2, 3, 4, 5, 1, 3, 5, 7, 7]
unique = []

for number in numbers:
    if number not in unique:
        unique.append(number)
print(unique)