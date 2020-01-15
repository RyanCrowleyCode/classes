from book import Book
from library import Library

book_one = Book("J.K. Rowling", "Harry Potter and the Sorcerer's Stone")

book_two = Book("J.K. Rowling", "Harry Potter and the Chamber of Secrets")

nss_library = Library("THE NSS LIBRARY")

nss_library.add_book(book_one)
nss_library.add_book(book_two)
nss_library.list_books()