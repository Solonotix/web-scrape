from datetime import date
from datetime import timedelta
from typing import Self
from typing import Sequence

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from selenium_pom import Locator
from .data import Precipitation
from .data import PrecipitationRecord
from .enum import StationFilterType
from .navbar import NavBar

YESTERDAY = date.today() - timedelta(days=1)


class DailyPrecipReports(NavBar):
    country_selection = Locator.css('select#frmPrecipReportSearch_ucStateCountyFilter_ddlCountry')
    country_selection_options = Locator.css('select#frmPrecipReportSearch_ucStateCountyFilter_ddlCountry option')
    county_selection = Locator.css('select#frmPrecipReportSearch_ucStateCountyFilter_ddlCounty')
    county_selection_options = Locator.css('select#frmPrecipReportSearch_ucStateCountyFilter_ddlCounty option')
    units_selection = Locator.css('select#obsSwitcher_ddlObsUnits')
    units_selection_options = Locator.css('select#obsSwitcher_ddlObsUnits option')
    url = "https://www.cocorahs.org/ViewData/ListDailyPrecipReports.aspx"

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.data = list()

    def __iter__(self):
        return iter(self.data)

    @property
    def all_data(self, stop_date: date = YESTERDAY) -> Sequence[PrecipitationRecord]:
        num_of_days = (date.today() - stop_date).days
        days = (date.today() - timedelta(days=i) for i in range(num_of_days))

        for day in days:
            self.filter_by_date(day).search()
            table = self.find_element(Locator.css('table#ucReportList_ReportGrid'))
            self.data.extend(Precipitation(table.get_attribute('outerHtml')))

        return self.data

    @property
    def county_dropdown(self) -> WebElement:
        return self.find_element(self.county_selection)

    @property
    def date_range_start(self) -> WebElement:
        return self.find_element(Locator.css('input#frmPrecipReportSearch_ucDateRangeFilter_dcStartDate_t'))

    @property
    def date_range_stop(self) -> WebElement:
        return self.find_element(Locator.css('input#frmPrecipReportSearch_ucDateRangeFilter_dcEndDate_t'))

    def filter_by_date(self, start_date: date, end_date: date = None) -> 'DailyPrecipReports':
        self.date_range_start.send_keys(f'{start_date:%m%d%Y}')
        self.date_range_stop.send_keys(f'{end_date if end_date is not None else start_date:%m%d%Y}')
        return self

    def filter_by_precipitation(self) -> 'DailyPrecipReports':

        return self

    def filter_by_station(self, station: str, filter_type: StationFilterType) -> 'DailyPrecipReports':
        if (self.station_number_check.get_property('value') == 'on') == (filter_type is StationFilterType.Name):
            self.station_number_check.click()
        if self.station_name_check.get_property('value') != filter_type is StationFilterType.Number:
            self.station_number_check.click()

        self.station_input.send_keys(station)
        return self

    def search(self) -> Self:


    def select_country(self: 'DailyPrecipReports', country: str) -> 'DailyPrecipReports':
        return self.select_option(self.country_selection, self.country_selection_options,
                                  lambda element: country in element.text)

    def select_county(self: 'DailyPrecipReports', county: str) -> 'DailyPrecipReports':
        if self.county_dropdown.is_enabled():
            self.select_option(self.county_selection, self.county_selection_options, lambda opt: county in opt.text)

        return self

    def select_units(self: 'DailyPrecipReports', unit: str) -> 'DailyPrecipReports':
        return self.select_option(self.units_selection, self.units_selection_options,
                                  lambda element: unit in element.text or unit in element.get_attribute('value'))

    @property
    def station_input(self) -> WebElement:
        return self.find_element(Locator.css('input#frmPrecipReportSearch_ucStationTextFieldsFilter_tbTextFieldValue'))

    @property
    def station_name_check(self) -> WebElement:
        return self.find_element(
            Locator.css('input#frmPrecipReportSearch_ucStationTextFieldsFilter_cblTextFieldsToSearch_1'))

    @property
    def station_number_check(self) -> WebElement:
        return self.find_element(
            Locator.css('input#frmPrecipReportSearch_ucStationTextFieldsFilter_cblTextFieldsToSearch_0'))

    @property
    def units_selector(self) -> WebElement:
        return self.find_element(Locator.css('select#obsSwitcher_ddlObsUnits'))
