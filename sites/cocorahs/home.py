from .daily_precip import DailyPrecipReports
from .data_page import DataPage
from .navbar import NavBar


class Home(NavBar):
    url = 'https://www.cocorahs.org'

    def go_to_data(self) -> DataPage:
        self.navbar_link('View Data')
        return DataPage(self.driver)

    def go_to_daily_precipitation_reports(self) -> DailyPrecipReports:
        self.navbar_link('Daily Precip Reports')
        return DailyPrecipReports(self.driver)

