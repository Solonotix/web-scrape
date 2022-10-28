import re

from bs4 import BeautifulSoup

from .precipitation_record import PrecipitationRecord


class Precipitation(object):
    def __init__(self, html: str):
        self.soup = BeautifulSoup(html, 'html.parser')

    def __iter__(self):
        for tr in self.soup.find_all('tr', class_=re.compile('item', re.IGNORECASE)):
            yield PrecipitationRecord.from_tr(tr)
