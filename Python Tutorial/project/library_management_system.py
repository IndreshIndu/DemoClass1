'''

class Library:
    def __init__(self):
        self.noBooks = 0
        self.books = []
        
    def addBooks(self, book):
        self.books.append(book) 
        self.noBooks = len(self.books)
        
    def showInfo(self):
        print(f"The library has {self.noBooks} books. The books are")
        for book in self.books:
            print(book)
        
            
l1=Library()
l1.addBooks("Harry Potter 1")
l1.addBooks("Harry Potter 2")
l1.addBooks("Harry Potter 3")
l1.showInfo()
'''



class Book:
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, copies):
        book = Book(title, author, copies)
        self.books.append(book)
        print(f"Book '{title}' by {author} added to the library.")

    def display_books(self):
        print("\nLibrary Books:")
        for book in self.books:
            print(f"{book.title} by {book.author} - Copies: {book.copies}")

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title and book.copies > 0:
                book.copies -= 1
                print(f"You have borrowed '{title}'. Enjoy reading!")
                return
        print(f"Sorry, '{title}' is either not available or all copies are currently borrowed.")

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                book.copies += 1
                print(f"Thanks for returning '{title}'. We hope you enjoyed the book!")
                return
        print(f"Error: '{title}' is not part of our library.")

# Example usage:
if __name__ == "__main__":
    library = Library()

    library.add_book("The Great Gatsby", "F. Scott Fitzgerald", 5)
    library.add_book("To Kill a Mockingbird", "Harper Lee", 3)
    library.add_book("1984", "George Orwell", 2)

    library.display_books()

    library.borrow_book("The Great Gatsby")
    library.borrow_book("To Kill a Mockingbird")
    library.borrow_book("Animal Farm")  # This book is not in the library

    library.display_books()

    library.return_book("The Great Gatsby")
    library.return_book("Animal Farm")  # This book was not borrowed

    library.display_books()










































