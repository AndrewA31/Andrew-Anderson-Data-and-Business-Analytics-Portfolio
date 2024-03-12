

class Basket:
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
        print(f"Added '{book.title}' to the basket.")
    
    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print(f"Removed '{book.title}' from the basket.")
                break

    def display_basket(self, book):
        if self.books:
            for book in self.books:
                print(book)
        else:
            print("Your basket is empty.")

    
        