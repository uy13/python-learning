movies = [
    ("Eternal Sunshine of the Spotless Mind", 20000000),
    ("Memento", 9000000),
    ("Requiem for a Dream", 4500000),
    ("Pirates of the Caribbean: On Stranger Tides", 379000000),
    ("Avengers: Age of Ultron", 365000000),
    ("Avengers: Endgame", 356000000),
    ("Incredibles 2", 200000000)
]

num_movies = int(input("Enter how many films you want to add: "))

for _ in range(num_movies):
    movie_name = input("Enter movie name: ")
    budget = int(input("Enter movie budget: "))
    movies.append((movie_name, budget))

high_budget = []
total_budgets = 0
for movie in movies:
    total_budgets += movie[1]
average = total_budgets / len(movies)

for movie in movies:
    if movie[1] > average:
        high_budget.append(movie)
        over_cost = movie[1] - average
        print(f"{movie[0]} has budgets more than average budgets is: ${over_cost:,.2f}")

print(f"There were {len(high_budget)} movie has budgets more than average budget ")
