from typing import TypeVar

from selenium.webdriver.remote.webelement import WebElement

from selenium_pom import Locator
from .enum import StationFilterType
from .navbar import NavBar


TPrecipReports = TypeVar('TPrecipReports', bound='DailyPrecipReports')


class DailyPrecipReports(NavBar):
    country_selection = Locator.css('select#frmPrecipReportSearch_ucStateCountyFilter_ddlCountry')
    country_selection_options = Locator.css('select#frmPrecipReportSearch_ucStateCountyFilter_ddlCountry option')
    county_selection = Locator.css('select#frmPrecipReportSearch_ucStateCountyFilter_ddlCounty')
    county_selection_options = Locator.css('select#frmPrecipReportSearch_ucStateCountyFilter_ddlCounty option')
    units_selection = Locator.css('select#obsSwitcher_ddlObsUnits')
    units_selection_options = Locator.css('select#obsSwitcher_ddlObsUnits option')
    url = "https://www.cocorahs.org/ViewData/ListDailyPrecipReports.aspx"

    def filter_by_station(self, station: str, filter_type: StationFilterType) -> TPrecipReports:
        if (self.station_number_check.get_property('value') == 'on') == (filter_type is StationFilterType.Name):
            self.station_number_check.click()
        if self.station_name_check.get_property('value') != filter_type is StationFilterType.Number:
            self.station_number_check.click()

        return self

    def select_country(self: TPrecipReports, country: str) -> TPrecipReports:
        return self.select_option(self.country_selection, self.country_selection_options,
            lambda element: country in element.text
        )

    def select_county(self: TPrecipReports, county: str) -> TPrecipReports:
        self.wait(2, ignore_timeout=True)
        return self

    def select_units(self: TPrecipReports, unit: str) -> TPrecipReports:
        return self.select_option(self.units_selection, self.units_selection_options,
            lambda element: unit in element.text or unit in element.get_attribute('value')
        )

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
