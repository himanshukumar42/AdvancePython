class Text:
    def __init__(self, text):
        self.__text = text

    @property
    def text(self):
        return self.__text

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__text}')"


class TextEditor:
    def __init__(self, content=""):
        self.__content = content

    def write(self, text):
        self.__content += text

    def save(self):
        return Text(self.__content)

    def undo(self, memento: Text):
        self.__content = memento.text

    def redo(self, memento: Text):
        self.__content = memento.text

    def __str__(self):
        return self.__content


class TextHistory:
    def __init__(self):
        self.__undo = []
        self.__redo = []

    def push(self, memento: Text):
        self.__undo.append(memento)
        self.__redo.clear()

    def undo(self, editor: TextEditor):
        if not self.__undo:
            print("Nothing to undo")
            return
        memento = self.__undo.pop()
        self.__redo.append(editor.save())
        editor.undo(memento)

    def redo(self, editor: TextEditor):
        if not self.__redo:
            print("Nothing to redo")
            return
        memento = self.__redo.pop()
        self.__undo.append(editor.save())
        editor.redo(memento)


def main() -> None:
    editor = TextEditor()
    history = TextHistory()

    editor.write("hello world ")
    history.push(editor.save())

    editor.write("what is your name ")
    history.push(editor.save())

    editor.write("what are you doing")
    print(editor)

    history.undo(editor)
    print(editor)

    history.redo(editor)
    print(editor)

    history.undo(editor)
    print(editor)
    history.undo(editor)
    print(editor)


if __name__ == '__main__':
    main()
