import requests
from bs4 import BeautifulSoup

class SoupGenerator:
    def __init__(self, url_generator, headers) -> None:
        self.url_generator = url_generator
        self.headers = headers

    def __iter__(self):
        return self

    def __next__(self):
        url = next(self.url_generator)
        return self.__url_2_soup(url)

    def __url_2_soup(self, url):
        response = requests.get(url, headers=self.headers)
        soup = BeautifulSoup(response.content, "html.parser")
        return soup