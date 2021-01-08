from app import books

USER_CHOICE = '''

- 'b' for 5-star books
- 'c' for cheapest books
- 'n' to get the next available book from the catalogue
- 'q' to exit

Enter your choice: '''


def print_best_books():
    best_books = sorted(books, key=lambda x: x.rating * -1)[:15]  # sort by 10
    for book in best_books:
        print(book)


def print_cheapest_book():
    cheapest_books = sorted(books, key=lambda x: x.price)[:15]
    for book in cheapest_books:
        print(book)


books_generator = (x for x in books)


def get_next_book():
    print(next(books_generator))


user_choices = {
    'b': print_best_books,
    'c': print_cheapest_book,
    'n': get_next_book
}


def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input in ('b', 'c', 'n'):
            user_choices[user_input]()
        else:
            print('Please enter a valid command')
        user_input = input(USER_CHOICE)


menu()
