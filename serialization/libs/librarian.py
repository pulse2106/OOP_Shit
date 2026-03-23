
from  user import User
class Librarian(User):
    def __init__(self, pid, pname, pgroup,pempid):
        super().__init__(pid, pname, pgroup)
        self._empid=pempid

    def EmpID(self)->str:
        return  self._empid
    
    def manage_book(pBookID) -> bool:
        pass

    def manage_user(self,pUser:User,pAction:str) -> bool:
        pass

    def charge_overdue(self,pBookID,pUserID) -> bool:
        pass


