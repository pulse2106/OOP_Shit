class Book:
    def __init__(self, id, name):
        self._id = id
        self._name = name
   
    @property
    def ID(self):
        return self._id
   
    @property
    def Name(self):
        return self._name