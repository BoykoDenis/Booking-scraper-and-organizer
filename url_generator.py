from string import Template
import urllib.parse


class BookingListingURLGenerator:
    def __init__(self, locations, from_date=None, min_price="min", price_limit="max", meal=None, overall_price_limit=None, min_days=3, max_days=10):
        assert min_days
        assert max_days

        self.locations = locations
        self.from_date = from_date
        self.to_date = self.from_date + min_days
        self.price_limit = price_limit
        self.min_price = min_price
        self.is_nflt = False
        self.meal = meal
        self.overall_price_limit = overall_price_limit
        self.min_days = min_days
        self.max_days = max_days

        self.template_vars = {
            "ss": locations[0],
            "checkin_year": from_date.year if from_date is not None else None,
            "checkin_month": from_date.month if from_date is not None else None,
            "checkin_monthday": from_date.day if from_date is not None else None,
            "checkout_year": self.to_date.year if self.to_date is not None else None,
            "checkout_month": self.to_date.month if self.to_date is not None else None,
            "checkout_monthday": self.to_date.day if self.to_date is not None else None,
        }

        self.meals_ids = {
            "breakfast": "1",
            "all inclusive" : "4",
            "b and d" : "9"
        }

        self.location_counter = 0
        self.day_counter = self.min_days

        self.template_url = Template(
            "https://www.booking.com/searchresults.html?ss=$destination"\
                                +("&checkin_year=$checkin_year"\
                                +"&checkin_month=$checkin_month"\
                                +"&checkin_monthday=$checkin_monthday" if self.from_date is not None else "")
                                +("&checkout_year=$checkout_year"\
                                +"&checkout_month=$checkout_month"\
                                +"&checkout_monthday=$checkout_monthday" if self.to_date is not None else "")
        )

    def __generate_url(self):
        url = self.template_url.safe_substitute(self.template_vars)
        url = self.__add_nflt(url)
        if self.min_price != "min" or self.price_limit != "max" or self.overall_price_limit is not None:
            url = self.__add_price(url)

        if self.meal is not None:
            url = self.__add_meal(url)
        return url

    def __add_nflt(self, url):
        if not self.is_nflt:
            url += "&nflt="
            self.is_nflt = True
        return url

    def __add_price(self, url):
        daily_price_limit = self.price_limit
        if self.price_limit=="max":
            daily_price_limit = self.overall_price_limit // self.day_counter
        url += f"price%3DCZK-{self.min_price}-{daily_price_limit}-1%3B"
        return url

    def __add_meal(self, url):
        url += f"mealplan%3D{self.meals_ids[self.meal]}%3B"
        return url

    def __iter__(self):
        return self

    def __next__(self):
        if self.location_counter >= len(self.locations):
            raise StopIteration
        else:
            self.template_vars["destination"] = self.locations[self.location_counter]

            self.to_date = self.from_date + self.day_counter
            self.template_vars["checkout_year"] = self.to_date.year
            self.template_vars["checkout_month"] = self.to_date.month
            self.template_vars["checkout_monthday"] = self.to_date.day

            self.day_counter += 1
            if self.day_counter > self.max_days:
                self.day_counter = self.min_days
                self.location_counter += 1

            self.is_nflt = False
            return self.template_vars["destination"], self.__generate_url()