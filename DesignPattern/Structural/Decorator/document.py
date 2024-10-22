from abc import ABC, abstractmethod


class Document(ABC):
    @abstractmethod
    def content(self):
        pass


class BasicDocument(Document):
    def content(self):
        return "This is a content in Document"


class DocumentDecorator(Document, ABC):
    def __init__(self, document: BasicDocument):
        self.document = document

    @abstractmethod
    def content(self):
        pass


class HeaderDecorator(DocumentDecorator):
    def content(self):
        return "Header\n" + self.document.content()


class FooterDecorator(DocumentDecorator):
    def content(self):
        return self.document.content() + "\nFooter."


def main() -> None:
    document = BasicDocument()

    header_document = HeaderDecorator(document)
    footer_document = FooterDecorator(header_document)
    print(footer_document.content())


if __name__ == '__main__':
    main()
