s = "---1--2-3--------------4---"

s = s.replace('-', ' ')
ans = s.split()
print(ans)
ans = list(map(int, ans))
print(ans)

# res = []
#
# for val in ans:
#     if val != '':
#         res.append(val)
#
# print(res)
