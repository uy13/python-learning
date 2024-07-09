d = {}

print(type(d))

d['x'] = 100

print(d)

# d['x'] += 1
d['x'] = d['x'] + 1

print(d['x'])
d['a'] = 0

print(d)

# d = {
#     1: 100,
#     1: 1000
# }
#
# print(d)

x = d.setdefault('h', 10)

print(x)
print(d)

print('-' * 20)
# {'x': 101, 'a': 0, 'h': 10}
for key in d:
    print(key)

print('-' * 20)

for value in d.values():
    print(value)

print('-' * 20)
for key, value in d.items():
    print(key, value, sep=' | ')
