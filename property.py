class Property:
    def __init__(self, price=None, city=None, rating=None):
        self.price = price
        self.city = city
        self.rating = rating

    @staticmethod
    def property_div_2_property(property_div_soup):
        price = property_div_soup.find("span",{'data-testid': 'price-and-discounted-price'}).text
        city = property_div_soup.find("span",{"data-testid":"address"}).text
        big_rating_div = property_div_soup.find("div",{"data-testid":"review-score"})
        rating = big_rating_div.find("div",{"class" : "a447b19dfd"}).text
        print(price, city, rating)
        return Property(
            price=price,
            city=city,
            rating=rating
            )
