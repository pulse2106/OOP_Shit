class User:
    def __init__(self, pid: str, pname: str):
        self._id = pid
        self._name = pname
        self._books = []

    @property
    def ID(self):
        return self._id

    @property
    def Name(self):
        return self._name

    @property
    def Books(self):
        return self._books

    def scan(self) -> bool:
        pass

    def borrow_book(self, pBook_ID) -> bool:
        if len(self.Books) == 3:
            raise Exception("You have borrowed max")

        if pBook_ID in self.Books:
            raise Exception("You have already borrowed this book")

        self.Books.append(pBook_ID)
        return True

    def return_book(self, pBook_ID) -> bool:
        if len(self.Books) < 1:
            raise Exception("You dont have any books borrowed")

        self.Books.remove(pBook_ID)
        return True