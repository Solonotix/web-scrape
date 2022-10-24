from enum import Enum

from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import ElementNotSelectableException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import InsecureCertificateException
from selenium.common.exceptions import InvalidCookieDomainException
from selenium.common.exceptions import InvalidCoordinatesException
from selenium.common.exceptions import InvalidElementStateException
from selenium.common.exceptions import InvalidSwitchToTargetException
from selenium.common.exceptions import JavascriptException
from selenium.common.exceptions import MoveTargetOutOfBoundsException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchShadowRootException
from selenium.common.exceptions import NoSuchAttributeException
from selenium.common.exceptions import NoSuchFrameException
from selenium.common.exceptions import NoSuchWindowException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import UnableToSetCookieException
from selenium.common.exceptions import UnexpectedAlertPresentException


class IgnorableExceptions(Enum):
    """Enum containing all ignorable errors for use in Selenium WebDriverWait operations"""
    
    """The element receiving the click event is obscuring the element that was requested to be clicked."""
    ElementClickInterceptedException = ElementClickInterceptedException
    """Thrown when interactions with an element in the DOM will hit another element due to paint order"""
    ElementNotInteractableException = ElementNotInteractableException
    """Thrown when trying to select an unselectable element. For example, selecting a 'script' element."""
    ElementNotSelectableException = ElementNotSelectableException
    """
    Thrown when an element is present on the DOM, but it is not visible, and so is not able to be interacted with.
    Most commonly encountered when trying to click or read text of an element that is hidden from view.
    """
    ElementNotVisibleException = ElementNotVisibleException
    """Navigation triggered a certificate warning, typically caused by an expired or invalid TLS certificate."""
    InsecureCertificateException = InsecureCertificateException
    """Thrown when attempting to add a cookie under a different domain than the current URL."""
    InvalidCookieDomainException = InvalidCookieDomainException
    """The coordinates provided to an interaction's operation are invalid."""
    InvalidCoordinatesException = InvalidCoordinatesException
    """
    Thrown when a command could not be completed because the element is in an invalid state.
    This can be caused by attempting to clear an element that isn't both editable and resettable.
    """
    InvalidElementStateException = InvalidElementStateException
    """Thrown when frame or window target to be switched doesn't exist."""
    InvalidSwitchToTargetException = InvalidSwitchToTargetException
    """An error occurred while executing JavaScript supplied by the user."""
    JavascriptException = JavascriptException
    """Thrown when the target provided to the `ActionsChains` move() method is invalid, i.e. out of document."""
    MoveTargetOutOfBoundsException = MoveTargetOutOfBoundsException
    """
    Thrown when switching to no presented alert.
    This can be caused by calling an operation on the Alert() class when an alert is not yet on the screen.
    """
    NoAlertPresentException = NoAlertPresentException
    """
    Thrown when the attribute of element could not be found.

    You may want to check if the attribute exists in the particular browser you are testing against.
    Some browsers may have different property names for the same property. 
    (IE8's .innerText vs. Firefox .textContent)
    """
    NoSuchAttributeException = NoSuchAttributeException
    """Thrown when frame target to be switched doesn't exist."""
    NoSuchFrameException = NoSuchFrameException
    """Thrown when trying to access the shadow root of an element when it does not have a shadow root attached."""
    NoSuchShadowRootException = NoSuchShadowRootException
    """
    Thrown when window target to be switched doesn't exist.
    To find the current set of active window handles, you can get a list of the active window handles by using::
        print driver.window_handles
    """
    NoSuchWindowException = NoSuchWindowException
    """
    Thrown when a reference to an element is now "stale".
    Stale means the element no longer appears on the DOM of the page.
    Possible causes of StaleElementReferenceException include, but not limited to:
        * You are no longer on the same page, or the page may have refreshed since the element was located.
        * The element may have been removed and re-added to the screen, since it was located.
          Such as an element being relocated.
          This can happen typically with a javascript framework when values are updated and the node is rebuilt.
        * Element may have been inside an iframe or another context which was refreshed.
    """
    StaleElementReferenceException = StaleElementReferenceException
    """Thrown when a driver fails to set a cookie."""
    UnableToSetCookieException = UnableToSetCookieException
    """
    Thrown when an unexpected alert has appeared.
    Usually raised when  an unexpected modal is blocking the webdriver from executing commands.
    """
    UnexpectedAlertPresentException = UnexpectedAlertPresentException
            