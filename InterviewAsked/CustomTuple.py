class CustomTuple:
    def __init__(self, *args):
        self.__elements = list(args)

    def __getitem__(self, index):
        if index < 0 or index >= len(self.__elements):
            raise IndexError("Index out of range")
        return self.__elements[index]

    def __len__(self):
        return len(self.__elements)

    def __repr__(self):
        return f"CustomTuple{tuple(self.__elements)}"

    def __iter__(self):
        return iter(self.__elements)

    def __contains__(self, item):
        return item in self.__elements

    def __hash__(self):
        return hash(tuple(self.__elements))

    def __eq__(self, other):
        if not isinstance(other, CustomTuple):
            return False
        return self.__elements == other

    def __setitem__(self, key, value):
        raise TypeError("'CustomTuple' object does not support item assignment")

    def __delitem__(self, key):
        raise TypeError("'CustomTuple' object does not support item deletion")
