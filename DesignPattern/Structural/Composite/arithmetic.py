# Arithmetic Expression Composite Design Pattern
from abc import ABC, abstractmethod


class Arithmetic(ABC):
    @abstractmethod
    def evaluate(self):
        pass


class Number(Arithmetic):
    def __init__(self, value):
        self.value = value

    def evaluate(self):
        return self.value


class Expression(Arithmetic):
    def __init__(self, left_expression, right_expression, operation):
        self.left_expression = left_expression
        self.right_expression = right_expression
        self.operation = operation

    def evaluate(self):
        if self.operation == "+":
            return self.left_expression.evaluate() + self.right_expression.evaluate()
        elif self.operation == "-":
            return self.left_expression.evaluate() - self.right_expression.evaluate()
        elif self.operation == "*":
            return self.left_expression.evaluate() * self.right_expression.evaluate()
        elif self.operation == "/":
            return self.right_expression.evaluate() / self.right_expression.evaluate()


def main() -> None:
    two = Number(2)
    one = Number(1)
    seven = Number(7)

    add = Expression(one, seven, "+")
    parent = Expression(two, add, "*")
    print(parent.evaluate())


if __name__ == '__main__':
    main()
