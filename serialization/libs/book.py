class Book:
    def __init__(self, id: str, title: str):
        self._id = id
        self._title = title
        self.is_available = True

    @property
    def ID(self):
        return self._id

    @property
    def Title(self):
        return self._title
    
    def __str__(self):
        return f"ID: {self._id}\n   -Name: {self._title}"
