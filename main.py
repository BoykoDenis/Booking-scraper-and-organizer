from bs4 import BeautifulSoup
import requests
import time

from url_generator import BookingListingURLGenerator
from property_parser import PropertyParser
from property import Property
from soup_gen import SoupGenerator
from date import Date

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0"}
"""
url = "https://www.booking.com/searchresults.html?\
        ss=Croatia&\
        map=1&\
        efdco=1&\
        label=gen173nr-1FCAEoggI46AdIM1gEaDqIAQGYATG4ARfIAQzYAQHoAQH4AQKIAgGoAgO4ApOW1rQGwAIB0gIkYWViNWMyMDgtOTAwYy00YzhiLWI0MGYtMjUyNjc1ZWViZDlh2AIF4AIB&aid=304142&\
        lang=en-us&\
        sb=1&\
        src_elem=sb&\
        src=index&\
        dest_id=54&\
        dest_type=country&\
        ac_position=0&\
        ac_click_type=b&\
        ac_langcode=en&\
        ac_suggestion_list_length=5&\
        search_selected=true&\
        search_pageview_id=5f629249e0670145&\
        ac_meta=GhA1ZjYyOTI0OWUwNjcwMTQ1IAAoATICZW46BGNocm9AAEoAUAA%3D&\
        ltfd=6%3A10%3A8-2024%3A1%3A1&\
        group_adults=2&no_rooms=1\
        &group_children=0\
        #map_closed"
"""

#url = "https://www.booking.com/searchresults.html?ss=Italy&ssne=Croatia&ssne_untouched=Croatia&label=gen173nr-1FCAEoggI46AdIM1gEaDqIAQGYATG4ARfIAQzYAQHoAQH4AQKIAgGoAgO4ApOW1rQGwAIB0gIkYWViNWMyMDgtOTAwYy00YzhiLWI0MGYtMjUyNjc1ZWViZDlh2AIF4AIB&aid=304142&lang=en-us&sb=1&src_elem=sb&src=searchresults&dest_id=104&dest_type=country&ac_position=0&ac_click_type=b&ac_langcode=en&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=e9d69846fded025f&ac_meta=GhBlOWQ2OTg0NmZkZWQwMjVmIAAoATICZW46BWl0YWx5QABKAFAA&checkin=2024-08-03&checkout=2024-08-13&ltfd=6%3A10%3A8-2024%3A1%3A1&group_adults=2&no_rooms=1&group_children=0"
#response = requests.get(url, headers=headers)

#soup = BeautifulSoup(response.content)
#all_soup_inner = soup.find_all("div", {'id': 'bodyconstraint-inner'})[0]
#all_properties_divs=all_soup_inner.find_all("div", class_="b9687b0063")[0].find_all("div", class_="d830fa48ad db402c28f2")[0].find_all("div", class_="f9958fb57b")[0].find_all("div", {'data-testid': 'property-card'})

from_date = Date("2024-08-03")
to_date = Date("2024-08-13")
urls_gen = BookingListingURLGenerator(["Croatia", "Paris"], from_date, to_date, 1000)
soup_gen = SoupGenerator(urls_gen, headers)
property_parser = PropertyParser(soup_gen)