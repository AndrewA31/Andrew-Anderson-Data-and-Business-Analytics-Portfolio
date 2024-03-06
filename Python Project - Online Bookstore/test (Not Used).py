class Book:
    def __init__(self, title, genre, author, price):
        self.title = title
        self.genre = genre
        self.author = author
        self.price = price

with open('books.txt', 'r') as file:
    books = []
    for line in file:
        components = line.strip().split(',')
        if len(components) == 4:
            book = Book(components[0], components[1], components[2], components[3])
            books.append(book)
for book in books:
    print(book.title,book.author)