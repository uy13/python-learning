number = int(input("Please enter a number: "))
a = range(10)
# print(number in set(range(10))
if number < a[0]:
    print("Too low")
elif number > a[-1]:
    print("Too high")
else:
    print("Yes")
