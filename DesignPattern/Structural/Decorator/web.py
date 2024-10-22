from abc import ABC, abstractmethod


class WebPage(ABC):
    @abstractmethod
    def render(self):
        pass


class BasicWebPage(WebPage):
    def render(self):
        return "Rendering a basic web page Example"


class WebPageDecorator(WebPage, ABC):
    def __init__(self, page: WebPage):
        self._page = page

    @abstractmethod
    def render(self):
        pass


def main() -> None:
    pass


if __name__ == '__main__':
    main()
