movies = [("Bo Gia", "Tran Thanh", "2021", "$17,000,000")]
print(movies)

title = input("Title: ")
title = title.strip()
title = title.title()

director = input("Director: ")
director = director.strip()
director = director.title()

release_year = input("Release year: ")
budget = input("Budget: ")

new_movies = title, director, release_year, budget
print(movies)
movies.append(new_movies)
print(f"{movies[0]} {movies[1]} ")
print(movies)

print(movies[0])
print(movies[1])

# movies.remove(movies[0])
movies.pop(0)
print(movies)
