from copy import deepcopy, copy


class Comment:
    def __init__(self, id: int, text: str):
        self.id: int = id
        self.text: str = text
        self.replies: list = []

    def __repr__(self):
        return f"{self.__class__.__name__}(id={self.id}, text={self.text}, replies={self.replies})"


def main() -> None:
    comment1 = Comment(1, "I just subscribed")
    comment2 = deepcopy(comment1)
    print(comment1)
    print(comment2)
    comment1.replies.append(10)
    comment1.text = "New comment"
    print(comment1)
    print(comment2)


if __name__ == '__main__':
    main()
