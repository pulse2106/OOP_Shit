from member import Member

class Student(Member):
    def calculate_fine(self, days_late):
        return days_late * 1