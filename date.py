class Date:
    def __init__(self, date_str):
        self.year = None
        self.month = None
        self.day = None

        self.attributes = ["year", "month", "day"]
        self.from_ios(date_str)

    def from_ios(self, str):
        ios_date = str.split("-")
        for i, sub_date in enumerate(ios_date):
            setattr(self, self.attributes[i], sub_date)