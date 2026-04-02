from member import Member

class FineCalculator:
    def calculate(self, member: Member, days_late):
        return member.calculate_fine(days_late)