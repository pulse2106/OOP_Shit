
class User():
    def __init__(self,pid,pname,pgroup):

        self._id=pid
        self._name=pname
        self._group=pgroup
    
    @property
    def ID(self):
        return self._id

    @property
    def Name(self):
        return self._name

    @property
    def Group(self):
        return self._group


    def scan(self)->bool:
        pass

    def borrow_book(self,pBookID)->bool:
        pass

    def return_book(self,pBookID)->bool:
        pass