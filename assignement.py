class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book_name):
        self.books.append(book_name)
        print(f"Book '{book_name}' added successfully.")

    def display_books(self):
        if not self.books:
            print("No books available in the library.")
        else:
            print("Books in Library:")
            for book in self.books:
                print("-", book)


# Initial test
if __name__ == "__main__":
    library = Library()
    library.add_book("Python Programming")
    library.display_books()