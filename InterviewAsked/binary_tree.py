class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class Tree:
    def __init__(self, root=None):
        self.root = root

    def add(self, value):
        if self.root is None:
            node = Node(value)
            self.root = node
            return
        current = self.root
        while True:
            if value < current.data:
                if current.left is None:
                    current.left = Node(value)
                    break
                else:
                    current = current.left
            else:
                if current.right is None:
                    current.right = Node(value)
                    break
                else:
                    current = current.right

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.data, end=" ")
            self.inorder(node.right)

    def preorder(self, node):
        if node:
            print(node.data, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data, end=" ")

    def longest_path(self, root):
        if self.root is None:
            return []

        if self.root.left:
            left_tree = self.root.left.longest_path()
        if self.root.right:
            right_tree = self.root.right.longest_path()

        if len(left_tree) > len(right_tree):
            left_tree.append(self.root.data)
        else:
            right_tree.append(self.root.data)

        if len(left_tree) > len(right_tree):
            return left_tree
        return right_tree


def main() -> None:
    tree = Tree()
    tree.add(4)
    tree.add(3)
    tree.add(6)
    tree.add(5)
    tree.add(7)

    tree.inorder(tree.root)
    print(tree.longest_path())


if __name__ == '__main__':
    main()
