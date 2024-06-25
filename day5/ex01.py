a = [1, 2, 3]
print(id(a))

b = [1, 2, 3]
print(id(b))

c = a
print(id(c))
print(a is c)

print(a == b and b == c)
