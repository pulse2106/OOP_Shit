
### overloaded with many responsibilities, violates the Single Responsibility Principle
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def save_to_file(self):
        print("Saving book to file...")

    def print_book(self):
        print(f"{self.title} by {self.author}")

    def lend_book(self, member):
        print(f"Lending book to {member}")