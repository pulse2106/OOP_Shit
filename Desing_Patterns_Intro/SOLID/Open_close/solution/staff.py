from member import Member

class Staff(Member):
    def calculate_fine(self, days_late):
        return days_late * 0.5