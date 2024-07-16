class Property:
    def __init__(self, div, price=None, country=None, city=None, rating=None):
        self.price = price
        self.country = country
        self.city = city
        self.rating = rating
        self.div = div

    @staticmethod
    def property_div_2_property(property_div_soup, country="unknown"):
        price = property_div_soup.find("span",{'data-testid': 'price-and-discounted-price'}).text
        city = property_div_soup.find("span",{"data-testid":"address"}).text
        big_rating_div = property_div_soup.find("div",{"data-testid":"review-score"})
        rating = big_rating_div.find("div",{"class" : "a447b19dfd"}) if big_rating_div else None

        rating = rating.text if rating else "No rating"

        print(price, city, rating)
        return Property(
            div=property_div_soup,
            price=price,
            country=country,
            city=city,
            rating=rating
            )
