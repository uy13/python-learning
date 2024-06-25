# t = 1, 2, 3, 4
# t = (1, 2, 3, 4)
# t = 1,
# t = (1,)
# t = (1)
# t = 1.
# print(type(t))

#      0  1  2  3          - index/position
#     -4 -3 -2 -1
tup = (1, 2, 3, 4)       # - value
print(id(tup))

print(tup[0])
print(tup[-len(tup)])
print(tup[len(tup)-1])
print(tup[-1])
# tup[0] = 1000 - error

# print(tup.index(100))
tup = tup + (100,)
print(id(tup))
print(tup)
