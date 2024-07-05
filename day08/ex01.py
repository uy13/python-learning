import random

target_number = random.randint(1, 100)

while True:
    number = int(input("Please guess a number: "))
    if number > target_number:
        print("Too high")
    elif number < target_number:
        print("Too low")
    else:
        print("You guess correctly")
        break
