movies = [
    ("Eternal Sunshine of the Spotless Mind", 20000000),
    ("Memento", 9000000),
    ("Requiem for a Dream", 4500000),
    ("Pirates of the Caribbean: On Stranger Tides", 379000000),
    ("Avengers: Age of Ultron", 365000000),
    ("Avengers: Endgame", 356000000),
    ("Incredibles 2", 200000000)
]

total_budgets = 0
for movie in movies:
    total_budgets += movie[1]
average_budgets = total_budgets / len(movies)

for movie in movies:
    if movie[1] > average_budgets:
        over_cost = movie[1] - average_budgets
        print(f"{movie[0]} has budgets more than average budgets is: ${over_cost:,.2f}")
