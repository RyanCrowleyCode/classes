class Library:
    def __init__(self, name):
        self.name = name
        self.books = list()

    def set_address(self, address):
        self.address = address

    def list_books(self):
        for book in self.books:
            print(f'"{book.title}" by {book.author}')

    def add_book(self, new_book):
        self.books.append(new_book)

if __name__ == '__main__':
    print("This runs when you run library.py directly, not when you run a file that imports library.py")
