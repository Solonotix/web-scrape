from typing import Callable
from typing import Self

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


from .Locator import Locator
from .PageWait import PageWait


class BasePage(object):
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.keys = Keys

    def __enter__(self) -> Self:
        return self

    def __exit__(self):
        self.driver.quit()

    def click_element(self, locator: Locator) -> Self:
        """
        Clicks the element as found on the page
        :param locator: Element to be clicked
        :type locator: Locator
        :return: The current page
        :rtype: self
        """
        self.find_element(locator).click()
        return self

    def find_element(self, locator: Locator) -> WebElement:
        """
        Returns the element as found on the page
        :param locator: Reference to element on page
        :type locator: Locator
        :return: The WebElement if found
        :rtype: WebElement
        """
        return self.driver.find_element(*locator)

    def find_elements(self, locator: Locator) -> list[WebElement]:
        """
        Returns the elements as found on the page
        :param locator: Reference to elements on the page
        :type locator: Locator
        :return: One or more WebElements if found, otherwise an empty list
        :rtype: list[WebElement]
        """
        return self.driver.find_elements(*locator)

    @property
    def html(self) -> str:
        """
        Returns the HTML source for the current page
        :return: The HTML source text
        :rtype: str
        """
        return self.driver.page_source

    def select_option(self, dropdown: Locator, options: Locator, action: Callable[[WebElement], bool]) -> Self:
        """
        Interaction with dropdown menus, selecting the requested option
        :param dropdown: Reference to the dropdown menu
        :type dropdown: Locator
        :param options: Reference to the options to be selected
        :type options: Locator
        :param action: Function to filter the options elements
        :type action: Callable[[WebElement, bool]
        :return: The current page
        :rtype: self
        """
        self.click_element(dropdown)
        for option in self.find_elements(options):
            if action(option):
                option.click()

        return self

    def send_keys(self, locator: Locator, keys: str) -> Self:
        """
        Type the provided string at the specified element
        :param locator: Target element to type into
        :type locator: Locator
        :param keys: Values to send to the element
        :type keys: str
        :return: The current page
        :rtype: self
        """
        self.find_element(*locator).send_keys(keys)
        return self

    def wait(self, seconds: float, *, ignore_timeout: bool = False) -> PageWait:
        """

        :param seconds: How long to wait before aborting
        :type seconds: float
        :param ignore_timeout: Whether to catch a TimeoutException
        :type ignore_timeout: bool
        :return: The PageWait helper class for building a Selenium wait
        :rtype: PageWait
        """
        if ignore_timeout:
            try:
                return PageWait(self.driver, seconds)
            except TimeoutException:
                pass
        else:
            return PageWait(self.driver, seconds)
