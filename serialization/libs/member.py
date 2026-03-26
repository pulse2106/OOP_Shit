
from libs.user import User

class Member(User):
    def __init__(self,pid,pname,pgroup):
        super.__init__(pid,pname,pgroup)
        ### do the member specific stuff

    def scan(self)->bool:
        pass

    def borrow_book(self,pBookID)->bool:
        pass

    def return_book(self,pBookID)->bool:
        pass