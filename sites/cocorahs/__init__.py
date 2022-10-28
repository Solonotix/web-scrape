from typing import Sequence

from selenium.webdriver.remote.webdriver import WebDriver

from .daily_precip import DailyPrecipReports
from .data import PrecipitationRecord
from .home import Home
from .navbar import NavBar


def get_data(driver: WebDriver) -> Sequence[PrecipitationRecord]:
    driver.get(Home.url)
    Home(driver).navbar_link('Daily Precip')
    return DailyPrecipReports(driver).all_data
