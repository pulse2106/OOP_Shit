
from lending import Lending

class LibrarySystem:
    def __init__(self):
        self.books = []
        self.members = []
        self.lendings = []

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def lend_book(self, book_id, member_id):
        book = next((b for b in self.books if b.book_id == book_id), None)
        member = next((m for m in self.members if m.member_id == member_id), None)

        if book and member and book.is_available:
            lending = Lending(book, member)
            self.lendings.append(lending)
            book.is_available = False
            print("Book lent successfully")
        else:
            print("Opps...Cannot lend book")

    def show_data(self):
        print("\n--- Books ---")
        for b in self.books:
            print(b)

        print("\n--- Members ---")
        for m in self.members:
            print(m)

        print("\n--- Lendings ---")
        for l in self.lendings:
            print(l)