menu = """Please enter one of the following options:

- 'a' to add a book
- 'l' to list the books
- 'f' to find a book
- 'q' to quit

What would you like to do? """


def add_book():
    title = input("please enter title: ").title().strip()
    author = input("please enter author: ").title().strip()
    year = input("please enter year: ").title().strip()
    with open("book.csv", "a") as book_list:
        book_list.write(f"{title},{author},{year}\n")


def get_all_books():
    books = []
    with open("book.csv", "r") as lst:
        for book in lst:
            title, author, year = book.strip().split(",")
            books.append({"title": title,
                          "author": author,
                          "year": year})

    return books


def show_books(book_list):
    if len(book_list) == 0:
        print("Empty!")

    else:
        for book in book_list:
            print(f"{book['title']} by {book['author']} in {book['year']}")


def find_book():
    all_books = get_all_books()
    found = []

    title = input("please enter your title book: ").lower()
    for book in all_books:
        if title in book["title"].lower():
            found.append(book)

    if len(found) != 0:
        show_books(found)
    else:
        print("Not found!")


option = input(menu)

while option != 'q':
    if option == 'a':
        add_book()
    elif option == 'l':
        books = get_all_books()
        show_books(books)
    elif option == 'f':
        find_book()
    else:
        print("Invalid option")
    option = input(menu)
