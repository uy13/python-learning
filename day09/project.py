card_numbers = list(input("Please enter your card number: ").strip())
checking_digit = card_numbers.pop()

card_numbers.reverse()

new_card_numbers = []

for index, number in enumerate(card_numbers):
    res = int(number)

    if index % 2 == 0:
        ans = res * 2
        if ans > 9:
            ans -= 9
        res = ans

    new_card_numbers.append(res)
total = int(checking_digit) + sum(new_card_numbers)
# if total % 10 == 0:
#     print("Valid")
# else:
#     print("invalid")
print("Valid" if total % 10 == 0 else "Invalid")
