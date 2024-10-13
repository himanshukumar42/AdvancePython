import inspect
from pprint import pprint
from dataclasses import dataclass, asdict, astuple, replace, field


@dataclass(order=True, slots=True)
class Comment:
    id: int
    text: str
    replies: list[int] = field(default_factory=list, compare=False, hash=False, repr=False)


def main() -> None:
    comment = Comment(1, "I just subscribed")
    print(comment)
    print(astuple(comment))
    print(asdict(comment))

    # pprint(inspect.getmembers(Comment, inspect.isfunction))
    copied_comment = replace(comment, id=2)
    print(copied_comment)


if __name__ == '__main__':
    main()
