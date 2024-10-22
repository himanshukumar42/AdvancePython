from abc import ABC, abstractmethod


class TextAbstract(ABC):
    @abstractmethod
    def format(self):
        pass


class Text(TextAbstract):
    def __init__(self, content):
        self.content = content

    def format(self):
        return self.content


class BoldDecorator(TextAbstract):
    def __init__(self, text: TextAbstract):
        self._text = text

    def format(self):
        return f"<b>{self._text.format()}</b>"


class ItalicDecorator(TextAbstract):
    def __init__(self, text: TextAbstract):
        self._text = text

    def format(self):
        return f"<i>{self._text.format()}</i>"


def main() -> None:
    text = Text("Hello World!")
    bold_text = BoldDecorator(text)
    italic_bold_text = ItalicDecorator(bold_text)
    new_bold_text = BoldDecorator(italic_bold_text)
    print(new_bold_text.format())


if __name__ == '__main__':
    main()
