a = set()
a.update(["hieu", "linh", "nam"])
print(a)
b = {"hieu", "trung", "nguyen", "nam"}
print(a.union(b))
print(a.intersection(b))
print(a.symmetric_difference(b))
