class Book:
    def __init__(self, author, title):
        # Establish the properties of each book
        # with a default value
        self.title = title
        self.author = author
        self.publisher = ""
        self.current_page = 1
        self.year_published = 0
        self.currently_reading = False

    def start_reading(self):
        self.currently_reading = True
        print(f'You start reading {self.title} at page {self.current_page}')

    def stop_reading(self, page):
        self.current_page = page
        self.currently_reading = False
        print(f'You stopped reading {self.title} at page {self.current_page}')






