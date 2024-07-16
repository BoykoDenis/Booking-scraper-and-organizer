import copy

class Date:
    def __init__(self):
        self.year = None
        self.month = None
        self.day = None

        self.month_lengths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        self.attributes = ["year", "month", "day"]


    def from_ios(self, str):
        ios_date = str.split("-")
        for i, sub_date in enumerate(ios_date):
            setattr(self, self.attributes[i], int(sub_date))
        return self

    def __add__(self, days):
        """
        this operator is stupid as fuck, do not add more then like 28 days, for small additions only!!!
        """
        day, month, year = self.day, self.month, self.year

        day += days
        if day > self.month_lengths[self.month-1]:
            day -= self.month_lengths[self.month-1]
            month += 1
            if month > 12:
                month = 1
                year += 1

        new_date = Date()
        new_date.day, new_date.month, new_date.year = day, month, year
        return new_date