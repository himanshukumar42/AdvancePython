from dataclasses import dataclass


class ManualComment:
    def __init__(self, id: int, text: str) -> None:
        self.__id: int = id
        self.__text: str = text

    @property
    def id(self):
        return self.__id

    @property
    def text(self):
        return self.__text

    def __repr__(self):
        return f"{self.__class__.__name__}(id={self.id}, text={self.text})"

    def __eq__(self, other):
        if other.__class__ is self.__class__:
            return (self.id, self.text) == (other.id, other.text)
        else:
            return NotImplemented

    def __ne__(self, other):
        result = self.__eq__(other)
        if result is NotImplemented:
            return NotImplemented
        else:
            return not result


if __name__ == '__main__':
    pass
