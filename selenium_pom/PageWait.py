from re import Pattern
from typing import Self

from selenium.webdriver.support import expected_conditions as Until
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from .IgnorableExceptions import IgnorableExceptions
from .Locator import Locator


class PageWait(object):
    def __init__(self, driver: WebDriver, seconds: float):
        self.driver = driver
        self.seconds = seconds
        self.ignored = list()

    def disable(self, ignorable: IgnorableExceptions) -> Self:
        self.ignored.append(ignorable.value)
        return self

    @property
    def wait(self):
        return WebDriverWait(self.driver, self.seconds)

    def alert_is_present(self) -> bool:
        """
        An expectation for an alert to be present
        :raises TimeoutException: Thrown when a command does not complete in enough time.
        :return: True when an alert is present, False otherwise
        :rtype: bool
        """
        return self.wait.until(Until.alert_is_present())

    def element_attribute_includes(self, locator: Locator, attribute: str) -> bool:
        """
        An expectation for checking if the given attribute is included in the specified element.
        :param locator: Reference to element
        :type locator: Locator
        :param attribute: HTML attribute to inspect
        :type attribute: str
        :raises TimeoutException: Thrown when a command does not complete in enough time.
        :return: True if the attribute meets expectations, False otherwise
        :rtype: bool
        """
        return self.wait.until(Until.element_attribute_to_include(locator, attribute))

    def element_located_and_selected(self, locator: Locator) -> bool:
        """
        An expectation for the element to be located is selected.
        :param locator: Reference to element
        :type locator: Locator
        :raises TimeoutException: Thrown when a command does not complete in enough time.
        :return: True if the element is found and selected, False otherwise
        :rtype: bool
        """
        return self.wait.until(Until.element_located_to_be_selected(locator))

    def element_clickable(self, mark: Locator | WebElement) -> WebElement | False:
        """
        An expectation for checking an element is visible and enabled such that you can click it.
        :param mark: either a locator (text) or a WebElement
        :type mark: Locator
        :type mark: WebElement
        :raises TimeoutException: Thrown when a command does not complete in enough time.
        :return: The element if it is clickable, False otherwise
        :rtype: WebElement | bool
        """
        if isinstance(mark, Locator):
            return self.wait.until(Until.element_to_be_clickable(mark.tuple))
        return self.wait.until(Until.element_to_be_clickable(mark))

    def element_located_selection_state(self, locator: Locator, selected: bool) -> bool:
        """
        An expectation to locate an element and check if the selection state specified is in that state.
        :param locator: Reference to the element
        :type locator: Locator
        :param selected: Whether the element should be selected or not
        :type selected: bool
        :raises TimeoutException: Thrown when a command does not complete in enough time.
        :return: True if the element matches the expected state, False otherwise
        :rtype: bool
        """
        return self.wait.until(Until.element_located_selection_state_to_be(locator, selected))

    def element_selected(self, element: WebElement) -> bool:
        """
        An expectation for checking the element is selected.
        :param element: Element to inspect
        :type element: WebElement
        :raises TimeoutException: Thrown when a command does not complete in enough time
        :return: True if the element is selected, False otherwise
        :rtype: bool
        """
        return self.wait.until(Until.element_to_be_selected(element))

    def frame_available(self, locator: Locator) -> bool:
        """
        An expectation for checking whether the given frame is available to switch to.
        If the frame is available it switches the given driver to the specified frame.
        :param locator: used to find the element
        :type locator: Locator
        :raises TimeoutException: Thrown when a command does not complete in enough time.
        :return: True if the frame could be switched to, False otherwise
        :rtype: bool
        """
        return self.wait.until(Until.frame_to_be_available_and_switch_to_it(locator))

    def invisibility_of_element(self, element: WebElement) -> WebElement | True:
        """
        An expectation for checking that an element is either invisible or not present on the DOM.
        :param element: Element to inspect
        :type element: WebElement
        :raises TimeoutException: Thrown when a command does not complete in enough time
        :return: The element if it isn't visible, or True if the element is absent from the DOM
        :rtype: WebElement
        """
        return self.wait.until(Until.invisibility_of_element(element))

    def invisibility_of_locator(self, locator: Locator) -> WebElement | True:
        """
        An expectation for checking that an element is either invisible or not present on the DOM.
        :param locator: used to find the element
        :type locator: Locator
        :raises TimeoutException: Thrown when a command does not complete in enough time
        :return: The element if it isn't visible, or True if the element is absent from the DOM
        :rtype: WebElement
        """
        return self.wait.until(Until.invisibility_of_element(locator))

    def new_window(self, handles: list[str]) -> bool:
        return self.wait.until(Until.new_window_is_opened(handles))

    def number_of_windows_to_be(self, count: int) -> bool:
        """
        An expectation for the number of windows to be a certain value.
        :param count: Expected count
        :type count: int
        :raises TimeoutException: Thrown when a command does not complete in enough time
        :return: True if the count is as expected, False otherwise
        :rtype: bool
        """
        return self.wait.until(Until.number_of_windows_to_be(count))

    def presence_of_all_elements_located(self, locator: Locator) -> list[WebElement]:
        """
        An expectation for checking that there is at least one element present on a web page.
        :param locator: used to find the element
        :type locator: Locator
        :raises TimeoutException: Thrown when a command does not complete in enough time.
        :return: the list of WebElements once they are located
        :rtype: list
        """
        return self.wait.until(Until.presence_of_all_elements_located(locator))

    def presence_of_element_located(self, locator: Locator) -> WebElement:
        """
        An expectation for checking that an element is present on the DOM of a page.
        This does not necessarily mean that the element is visible.
        :param locator: used to find the element
        :type locator: Locator
        :raises TimeoutException: Thrown when a command does not complete in enough time.
        :return: WebElement once it is located
        :rtype: WebElement
        """
        return self.wait.until(Until.presence_of_element_located(locator))

    def staleness_of(self, element: WebElement) -> bool:
        """
        Wait until an element is no longer attached to the DOM. element is the element to wait for.
        :param element: The element to inspect
        :type element: WebElement
        :return: False if the element is still attached to the DOM, true otherwise.
        :rtype: bool
        """
        return self.wait.until(Until.staleness_of(element))

    def text_in_element(self, locator: Locator, text: str) -> bool:
        """
        An expectation for checking if the given text is present in the specified element.
        :param locator: used to find the element
        :type locator: Locator
        :param text: the fragment of text expected
        :type text: str
        :raises TimeoutException: Thrown when a command does not complete in enough time.
        :return: True when the element is located, and the text is present inside it. False otherwise
        :rtype: bool
        """
        return self.wait.until(Until.text_to_be_present_in_element(locator, text))

    def text_in_element_attribute(self, locator: Locator, attribute: str, text: str) -> bool:
        """
        An expectation for checking if the given text is present in the specified element's attribute.
        :param locator: used to find the element
        :type locator: Locator
        :param attribute: HTML attribute of the specified element
        :type attribute: str
        :param text: the fragment of text expected
        :type text: str
        :raises TimeoutException: Thrown when a command does not complete in enough time.
        :return: True when the element is located, and the text is present inside it. False otherwise
        :rtype: bool
        """
        return self.wait.until(Until.text_to_be_present_in_element_attribute(locator, attribute, text))

    def text_in_element_value(self, locator: Locator, text: str) -> bool:
        """
        An expectation for checking if the given text is present in the specified element's value attribute.
        :param locator: used to find the element
        :type locator: Locator
        :param text: the fragment of text expected
        :type text: str
        :raises TimeoutException: Thrown when a command does not complete in enough time.
        :return: True when the element is located, and the text is present inside it. False otherwise
        :rtype: bool
        """
        return self.wait.until(Until.text_to_be_present_in_element_value(locator, text))

    def title_contains(self, title: str) -> bool:
        """
        An expectation for checking that the title contains a case-sensitive substring.

        :param title: the fragment of title expected
        :type title: str
        :raises TimeoutException: Thrown when a command does not complete in enough time.
        :return: True when the title matches, False otherwise
        :rtype: bool
        """
        return self.wait.until(Until.title_contains(title))

    def title_is(self, title: str) -> bool:
        """
        An expectation for checking the title of a page.
        :param title: the expected title, which must be an exact match
        :type title: str
        :raises TimeoutException: Thrown when a command does not complete in enough time.
        :return: True if the title matches, false otherwise.
        :rtype: bool
        """
        return self.wait.until(Until.title_is(title))

    def url_changes(self, url: str) -> bool:
        """
        An expectation for checking the current url.
        :param url: the expected url, which must not be an exact match
        :type url: str
        :raises TimeoutException: Thrown when a command does not complete in enough time.
        :return: True if the url is different, false otherwise.
        :rtype: bool
        """
        return self.wait.until(Until.url_changes(url))

    def url_contains(self, url: str) -> str:
        """
        An expectation for checking that the current url contains a case-sensitive substring.
        :param url: the fragment of url expected
        :type url: str
        :raises TimeoutException: Thrown when a command does not complete in enough time.
        :return: True when the url matches, False otherwise
        :rtype: bool
        """
        return self.wait.until(Until.url_contains(url))

    def url_is(self, url: str) -> bool:
        """
        An expectation for checking the current url.
        :param url: the expected url, which must be an exact match
        :type url: str
        :raises TimeoutException: Thrown when a command does not complete in enough time.
        :return: True if the url matches, false otherwise.
        :rtype: bool
        """
        return self.wait.until(Until.url_to_be(url))

    def url_matches(self, pattern: Pattern) -> bool:
        """
        An expectation for checking the current url.
        :param pattern: the expected pattern, which must be an exact match
        :type pattern: Pattern
        :raises TimeoutException: Thrown when a command does not complete in enough time.
        :return: True if the url matches, false otherwise.
        :rtype: bool
        """
        return self.wait.until(Until.url_matches(pattern))

    def visibility_of(self, element: WebElement) -> WebElement:
        """
        An expectation for checking that an element, known to be present on the DOM of a page, is visible.
        Visibility means that the element is not only displayed but also has a height and width > 0.
        :param element: the WebElement
        :type element: WebElement
        :raises TimeoutException: Thrown when a command does not complete in enough time.
        :return: the (same) WebElement once it is visible
        :rtype: WebElement
        """
        return self.wait.until(Until.visibility_of(element))

    def visibility_of_all_elements_located(self, locator: Locator) -> False | list[WebElement]:
        """
        An expectation for checking that all elements are present on the DOM of a page and visible.
        Visibility means that the elements are not only displayed but also has a height and width > 0.

        :param locator: used to find the elements
        :return: the list of WebElements once they are located and visible
        :rtype: list[WebElement]
        """
        return self.wait.until(Until.visibility_of_all_elements_located(locator))

    def visibility_of_any_elements_located(self, locator: Locator) -> list[WebElement]:
        """
        An expectation for checking that there is at least one element visible on a web page.
        :param locator: is used to find the element
        :return: the list of WebElements once they are located
        :rtype: list[WebElement]
        """
        return self.wait.until(Until.visibility_of_any_elements_located(locator))

    def visibility_of_element_located(self, locator: Locator) -> WebElement:
        """
        An expectation for checking that an element is present on the DOM of apage and visible.
        Visibility means that the element is not only displayed but also has a height and width > 0.
        :param locator: used to find the element
        :type locator: Locator
        :raises TimeoutException: Thrown when a command does not complete in enough time.
        :return: the WebElement once it is located and visible
        :rtype: WebElement
        """
        return self.wait.until(Until.visibility_of_element_located(locator))