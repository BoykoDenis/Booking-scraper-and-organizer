from string import Template

class BookingListingURLGenerator:
    def __init__(self, locations, from_date=None, to_date=None, price_limit=None):
        self.locations = locations
        self.from_date = from_date
        self.to_date = to_date
        self.price_limit = price_limit

        self.template_vars = {
            "destination": locations[0],
            "checkin_year": from_date.year if from_date is not None else None,
            "checkin_month": from_date.month if from_date is not None else None,
            "checkin_day": from_date.day if from_date is not None else None,
            "checkout_year": to_date.year if to_date is not None else None,
            "checkout_month": to_date.month if to_date is not None else None,
            "checkout_day": to_date.day if to_date is not None else None,
            "max_price": price_limit
        }

        self.location_counter = 0
        self.template_url = Template(
            "https://www.booking.com/searchresults.html?ss=$destination"\
                                +("&checkin_year=$checkin_year"\
                                +"&checkin_month=$checkin_month"\
                                +"&checkin_monthday=$checkin_day" if self.from_date is not None else "")
                                +("&checkout_year=$checkout_year"\
                                +"&checkout_month=$checkout_month"\
                                +"&checkout_monthday=$checkout_day" if self.to_date is not None else "")
                                +("&nflt=price%3DCZK-min-$max_price-1" if self.price_limit is not None else "")
        )

    def __generate_url(self):
        url = self.template_url.safe_substitute(self.template_vars)
        return url

    def __iter__(self):
        return self

    def __next__(self):
        if self.location_counter >= len(self.locations):
            raise StopIteration
        else:
            self.template_vars["destination"] = self.locations[self.location_counter]
            self.location_counter += 1
            return self.__generate_url()