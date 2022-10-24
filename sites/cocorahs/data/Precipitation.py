from bs4 import BeautifulSoup


class Precipitation(object):
    def __init__(self, html: str):
        self.soup = BeautifulSoup(html, 'html.parser')
