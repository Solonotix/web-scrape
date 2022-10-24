from .daily_precip import DailyPrecipReport
from .navbar import NavBar


class Home(NavBar):
    url = 'https://www.cocorahs.org'

    def go_to_data(self) -> DataPage:
        self.navbar_link('View Data')

    def go_to_daily_precipitation_reports(self) -> DailyPrecipReport:
        self.navbar_link('Daily Precip Reports')
        return DailyPrecipReport(self.driver)

