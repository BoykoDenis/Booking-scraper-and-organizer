from property import Property

class PropertyParser:
    def __init__(self, soups):
        self.properties = self.__parse_soups(soups)

    def __parse_properties_from_soup(self, soup):
        property_divs = soup.find_all("div", {'data-testid': 'property-card-container'})
        properties = []
        for property_div in property_divs:
            properties.append(Property.property_div_2_property(property_div))

        return properties


    def __parse_soups(self, soups):
        properties = []
        for soup in soups:
            properties.extend(self.__parse_properties_from_soup(soup))

        return properties

