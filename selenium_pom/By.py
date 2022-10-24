from enum import Enum
from enum import unique

from selenium.webdriver.common.by import By as _By


@unique
class By(Enum):
    ClassName = _By.CLASS_NAME
    Css = _By.CSS_SELECTOR
    Id = _By.ID
    Link = _By.LINK_TEXT
    Name = _By.NAME
    PartialLink = _By.PARTIAL_LINK_TEXT
    Tag = _By.TAG_NAME
    XPath = _By.XPATH

    def __str__(self) -> str:
        return str(self.value)

    def __repr__(self) -> str:
        return f"<By.{self.name}: '{self.value}'"
