"""
list: []
index: 0
"""
#          0    1  2  3  4 - index/position
# 2 = 3 - 1 = len - 1
# -len: first
#          -5  -4 -3 -2 -1
numbers = [100, 1, 2, 3, 4]  # - value
print(type(numbers))
print(len(numbers))

print(numbers[0])  # 1
print(numbers[-len(numbers)])
print(numbers[-1])
"""
list
first: 0, -len
last: len - 1, -1
"""
length = len(numbers)
print(numbers[length - 1])

# change value
numbers[1] = 1000
print(numbers)
numbers[2] = 'a'
print(numbers)
numbers[-3] = 'c'
print(numbers)

numbers[2] = 10000
print(numbers)

# append
numbers.append(100)
print(numbers)

numbers.append(-100)
print(numbers)

# extend
numbers.extend([3, 4, 5])
print(numbers)

# numbers.append([3, 4, 5])
# print(numbers)

# insert
numbers.insert(1000, -123)
print(numbers)

# remove
# numbers.remove(345)
# print(numbers)

# # pop
# value = numbers.pop(2)
# print(value)
#
# print(numbers)

# del numbers[1000]
# print(numbers)

numbers.sort(reverse=True)
print(numbers)

numbers.reverse()
print(numbers)

count = numbers.count(3.)
print(count)

a = numbers.copy()
print(a == numbers)
print(a is numbers)

numbers.clear()
print(numbers)
