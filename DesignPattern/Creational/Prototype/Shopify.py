from copy import deepcopy


class StoreTheme:
    def __init__(self, layout=None, color=None, logo=None):
        self.layout = layout
        self.color = color
        self.logo = logo

    def clone(self):
        return deepcopy(self)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.layout}, {self.color}, {self.logo})"


def main() -> None:
    base_theme = StoreTheme("Standard Layout", "White", "Default Logo")

    store1_theme = base_theme.clone()
    store1_theme.color = "Blue"
    store1_theme.logo = "Store1 Logo"
    print(base_theme)
    print(store1_theme)
    print(base_theme == store1_theme)
    


if __name__ == '__main__':
    main()
