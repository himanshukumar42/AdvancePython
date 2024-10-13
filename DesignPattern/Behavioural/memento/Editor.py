class Text:
    def __init__(self, text):
        self.__text = text

    @property
    def text(self):
        return self.__text

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__text})"


class Editor:
    def __init__(self):
        self.__content = ""
        self.__history = TextHistory()
        self.__history.undo.append(self.save())

    def write(self, text):
        self.__history.undo.append(self.save())
        self.__content += text

    def save(self):
        return Text(self.__content)

    def undo(self):
        if len(self.__history.undo) == 0:
            print("Nothing to undo")
            return
        self.__history.redo.append(self.save())
        memento = self.__history.undo.pop()
        self.__content = memento.text

    def redo(self):
        if len(self.__history.redo) == 0:
            print("Nothing to redo")
            return
        self.__history.undo.append(self.save())
        memento = self.__history.redo.pop()
        self.__content = memento.text

    def __str__(self):
        return self.__content


class TextHistory:
    def __init__(self):
        self.__undo = []
        self.__redo = []

    @property
    def undo(self):
        return self.__undo

    @property
    def redo(self):
        return self.__redo


def main() -> None:
    editor = Editor()
    editor.write("Hello Himanshu ")
    editor.write("How are you ")
    editor.write("What are you doing")
    print(editor)
    editor.undo()
    print(editor)
    editor.undo()
    print(editor)
    editor.undo()
    print(editor, "hllo")
    editor.redo()
    print(editor)
    editor.redo()
    print(editor)
    editor.redo()
    print(editor)


if __name__ == '__main__':
    main()
