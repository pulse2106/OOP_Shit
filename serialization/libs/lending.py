from datetime import datetime

class Lending:
    def __init__(self, book, member):
        self.book = book
        self.member = member
        self.date = datetime.now()

    def __str__(self):
        return f"{self.book.Title} lent to {self.member.Name} on {self.date}"