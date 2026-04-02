
### what is the problem with this code?

class FineCalculator:
    def calculate(self, member_type, days_late):
        if member_type == "student":
            return days_late * 1
        elif member_type == "staff":
            return days_late * 0.5