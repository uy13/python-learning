book_list = []
menu = """Please enter one of the following options:

- 'a' to add a book
- 'l' to list the books
- 'q' to quit

What would you like to do? """
option = input(menu.strip())


def add():
    title = input("Enter title: ").strip().title()
    author = input("Enter author: ").strip().title()
    year = int(input("Enter year: "))
    lst = {"title": title, "author": author, "year": year}
    book_list.append(lst)


def list():
    for book in book_list:
        title, author, year = book.values()
        print(f"{title} by {author}, {year}")


while option != "q":
    if option == "a":
        add()
    elif option == "l":
        list()
    else:
        print("your option is invalid")
    option = input(menu).strip().lower()
