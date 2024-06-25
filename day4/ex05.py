movies = [("Bo Gia", "Tran Thanh", "2021", "$17,000,000")]
title = input("Title: ")
director = input("Director: ")
release_year = input("Release year: ")
budget = input("Budget: "+"$")

new_movies = title, director, release_year, budget
movies.append(new_movies)
print(movies)