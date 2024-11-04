class Book:
    def __init__(self, pages, author, price):
        self.__pages = pages
        self.__author = author
        self.__price = price
        self.public_numeric_field = 0
        self.public_string_field = ""

    def get_pages(self):
        return self.__pages

    def get_author(self):
        return self.__author

    def get_price(self):
        return self.__price

    def set_pages(self, pages):
        self.__pages = pages

    def set_author(self, author):
        self.__author = author

    def set_price(self, price):
        self.__price = price

    def __str__(self):
        return f"Book (Author: {self.get_author()}, Pages: {self.get_pages()}, Price: {self.get_price()} UAH)"

    def __repr__(self):
        return f"Book ('{self.get_author()}', {self.get_pages()}, {self.get_price()})"

    def __del__(self):
        print(f"Book '{self.get_author()}' is being deleted.")

def main():
    
    book1 = Book(300, "Taras Shevchenko", 150.00)
    book1.public_numeric_field = 1
    book1.public_string_field = "Classic Literature"

    book2 = Book(400, "Ivan Franko", 180.00)
    book2.public_numeric_field = 2
    book2.public_string_field = "Historical Prose"

    book3 = Book(200, "Lesya Ukrainka", 120.00)
    book3.public_numeric_field = 3
    book3.public_string_field = "Poetry"

    for book in (book1, book2, book3):
        print(book)

if __name__ == "__main__":
    main()
    
    