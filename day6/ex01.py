employees = [
    ("Rolf Smith", 35, 8.75),
    ("Anne Pun", 30, 12.50),
    ("Charlie Lee", 50, 15.50),
    ("Bob Smith", 20, 7.00)
]
for empoloyee in employees:
    pay = empoloyee[1] * empoloyee[2]
    print(f"{empoloyee[0]} has to be paid ${pay:.2f}")
