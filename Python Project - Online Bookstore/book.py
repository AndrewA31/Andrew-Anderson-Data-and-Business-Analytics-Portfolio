

class Book:
    def __init__(self, title, genre, author, price):
        self.title = title
        self.genre = genre
        self.author = author
        self.price = price

def book_search():
    with open('books.txt', 'r') as file:
            books = []
            for line in file:
                components = line.strip().split(',')
                if len(components) == 4:
                    book = Book(components[0], components[1], components[2], components[3])
                    books.append(book)

    def search_books(books, search_term):
        found_books = []
        search_term_lower = search_term.lower()
        for book in books:
            if (search_term_lower in book.title.lower() or
                search_term_lower in book.genre.lower() or
                search_term_lower in book.author.lower() or
                search_term_lower in str(book.price).lower()):
                found_books.append(book)
        return found_books

    print("**********************************************")
    print("*                Book Search                 *")
    print("**********************************************")
    search_term = input("Please enter a Title, Genre, or Author to search: ")
    results = search_books(books, search_term)
    return results

basket = []
def add_to_basket(book):
    add_book = input("Would you like to add this book to Basket? Y / N: ").lower()
    if add_book == 'y':
        basket.append(book)
        print(f"{book.title} added to basket.")

def empty_basket():
    basket.clear()

def add_book():
    books = book_search() 
    if books:
        if len(books) == 1:
            print(f"Title: {books[0].title}, Genre: {books[0].genre}, Author: {books[0].author}, Price: {books[0].price}")
            add_to_basket(books[0])
        else:
            print("Found multiple books:")
            for i, book in enumerate(books, start=1):
                print(f"{i}. Title: {book.title}, Genre: {book.genre}, Author: {book.author}, Price: {book.price}")
            while True:
                choice = input("Enter the number of the book you want to add to the basket, or enter '0' to return to the Menu: ")
                if choice == '0':
                    break
                try:
                    choice = int(choice)
                    if 1 <= choice <= len(books):
                        add_to_basket(books[choice - 1])  # Subtract 1 because of zero-based indexing
                        break
                    else:
                        print("Invalid choice. Please enter a valid number.")
                                           
                except ValueError:
                    print("Invalid input. Please enter a number.")
    else:
        print("No books found matching the search term, please try again.")