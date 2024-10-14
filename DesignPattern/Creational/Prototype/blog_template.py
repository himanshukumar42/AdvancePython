from copy import deepcopy


class BlogTemplate:
    def __init__(self, layout, font, theme_color):
        self.layout = layout
        self.font = font
        self.theme_color = theme_color

    def clone(self):
        return deepcopy(self)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.layout}, {self.font}, {self.theme_color})"


def main() -> None:
    basic_template: BlogTemplate = BlogTemplate("Two-Column", "Arial", "White")

    new_template = basic_template.clone()
    new_template.theme_color = "Magenta"
    new_template.font = "Times New Roman"


if __name__ == '__main__':
    main()
