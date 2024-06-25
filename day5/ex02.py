numbers = [1, 2, 3, 4]
print(id(numbers))

# numbers = numbers + [5]
numbers += [5]
print(id(numbers))

numbers.append(100)
print(id(numbers))
