# Search Books
def search_books(is_guest, books):
    search_criteria = input("Please enter a search criteria: (Title, Author, Genre, Height, Publisher): ").strip().capitalize()
    search_value = input(f"Enter the {search_criteria} to search: ").strip().lower()

    with open("books.csv", 'r') as csvfile:
        reader = csv.DictReader(csvfile, fieldnames=['Title', 'Author', 'Genre', 'Height', 'Publisher'])
        next(reader)
        found_books = []
        for row in reader:
            if row[search_criteria].strip().lower() == search_value:
                found_books.append(row)
        
        if found_books:
            print("Found Books:")
            for book in found_books:
                print(f"Title: {book['Title']}, Author: {book['Author']}, Genre: {book['Genre']}, Height: {book['Height']}, Publisher: {book['Publisher']}")
                add_book = input(f"Would you like to add {book['Title']} to your basket? Y or N: ").lower()
                if add_book == 'y':
                    Basket.add_book(book)
        else:
            print(f"No books found with {search_criteria} '{search_value}'")
            search_books(is_guest)
    return is_guest


def read_books():
    books = []
    with open("books.csv", 'r') as csvfile:
        reader = csv.DictReader(csvfile, fieldnames=['Title', 'Author', 'Genre', 'Height', 'Publisher'])
        for row in reader:
            title, author, genre, height, publisher = row
            books.append(Book(title, author, genre, height, publisher))
    return books