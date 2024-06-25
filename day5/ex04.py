hours = float(input("How many hours the employee worked this week: "))
hourly_wage = float(input("Hourly wage for this employee: $"))
if hours > 40:
    hours40 = 40 * hourly_wage
    ot = (hours - 40) * hourly_wage * 1.1
    total = hours40 + ot
    print(f"Total = {total:.2f}")
else:
    print(f"Total = {(hours * hourly_wage):.2f}")
