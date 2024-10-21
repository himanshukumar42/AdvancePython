from abc import ABC, abstractmethod


class UIComponent(ABC):
    @abstractmethod
    def render(self):
        pass


class Button(UIComponent):
    def __init__(self, label):
        self.label = label

    def render(self):
        return f"<button>{self.label}</button>"


class TextBox(UIComponent):
    def __init__(self, text: str):
        self.text = text

    def render(self):
        return f"<p>{self.text}</p>"


class Heading(UIComponent):
    def __init__(self, level: int,  text: str):
        self.level = level
        self.text = text

    def render(self):
        return f"<h{self.level}>{self.text}</h{self.level}>"


class Image(UIComponent):
    def __init__(self, src: str, alt: str):
        self.src = src
        self.alt = alt

    def render(self):
        return f"<img src=\"{self.src}\" alt=\"{self.alt}\">"


class Label(UIComponent):
    def __init__(self, name):
        self.name = name

    def render(self):
        return f"<label for=\"html\">{self.name}</label>"


class Input(UIComponent):
    def __init__(self, input_type, *args, **kwargs):
        self.input_type = input_type
        self.kwargs = kwargs

    def render(self):
        input_st = f"<input type=\"{self.input_type}\" "
        for key, val in self.kwargs.items():
            input_st += str(key) + "=\"" + str(val) + "\" "
        input_st += "/>"
        return input_st


class Div(UIComponent):
    def __init__(self, _id, _class):
        self._id = _id
        self._class = _class
        self._children = []

    def add(self, component: UIComponent):
        self._children.append(component)

    def remove(self, component: UIComponent):
        self._children.remove(component)

    def render(self):
        div_component = f"<div id=\"{self._id}\" class=\"{self._class}\">\n"
        for child in self._children:
            div_component += child.render() + "\n"
        div_component += "</div>\n"
        return div_component


def main() -> None:
    div1 = Div("mydiv", "outer")
    h2 = Heading(2, "My Heading")
    lab = Label("Enter text: ")
    inp = Input("text", id="myTextbox", placeholder="Type here....", style="margin-bottom: 10px; width: 100%;")
    but = Button("Submit")

    div1.add(h2)
    div1.add(lab)
    div1.add(inp)
    div1.add(but)

    print(div1.render())


if __name__ == '__main__':
    main()
