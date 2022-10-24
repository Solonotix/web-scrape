from typing import Tuple

from .By import By


class Locator(object):
    def __init__(self, by: By, value: str):
        self.by = by
        self.value = value

    def __iter__(self):
        yield str(self.by)
        yield self.value

    @classmethod
    def class_name(cls, value: str) -> 'Locator':
        return cls(By.ClassName, value)

    @classmethod
    def css(cls, value: str) -> 'Locator':
        return cls(By.Css, value)

    @classmethod
    def id(cls, value: str) -> 'Locator':
        return cls(By.Id, value)

    @classmethod
    def link(cls, value: str) -> 'Locator':
        return cls(By.Link, value)

    @classmethod
    def name(cls, value: str) -> 'Locator':
        return cls(By.Name, value)

    @classmethod
    def partial_link(cls, value: str) -> 'Locator':
        return cls(By.PartialLink, value)

    @classmethod
    def tag(cls, value: str) -> 'Locator':
        return cls(By.Tag, value)

    @property
    def tuple(self) -> Tuple[str, str]:
        return str(self.by), self.value

    @classmethod
    def xpath(cls, value: str) -> 'Locator':
        return cls(By.XPath, value)
