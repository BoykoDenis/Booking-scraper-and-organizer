from property import Property

class PropertyParser:
    def __init__(self, country_soups):
        self.properties = self.__parse_soups(country_soups)

    def __parse_properties_from_soup(self, country_soup, return_property_divs=False, country="unknown"):
        country, soup = country_soup
        property_divs_content = soup.find_all("div", {'data-testid': 'property-card-container'})
        properties = []
        for property_div in property_divs_content:
            properties.append(Property.property_div_2_property(property_div, country=country))

        return properties


    def __parse_soups(self, country_soups):
        properties = []
        for country_soup in country_soups:
            properties.extend(self.__parse_properties_from_soup(country_soup))

        return properties

    def __add_country(self, html, country):
        return html + f"<h1>{country}</h1>"

    def gen_html(self):
        html = "<html><head><link rel=\"stylesheet\" href=\"output.css\"></head><body>"
        for property in self.properties:
            for path in property.div.find_all('path'):
                path.decompose()

            for svg in property.div.find_all('svg'):
                svg.decompose()

            html = self.__add_country(html, property.country)
            html += property.div.prettify()
        html += "</body></html>"
        return html


