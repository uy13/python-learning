name = input("Enter employee's name: ")
name = name.strip()
name = name.title()

hourly_wage = float(input("What is their hourly wage? "))
hours_week = float(input("How many hours have they worked this week? "))

money = hourly_wage * hours_week
# ----------------------------------------------------
# print("-------------------------------------------------------------------------")
print('-' * 75)
print(f"{name} earned ${round(money, 2)} this week")
print(f"{name} earned ${money:.2f} this week")
print(f"{name} earned ${format(money, '.2f')} this week")
