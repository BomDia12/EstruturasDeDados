import ast


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def height(self):
        def recursive(node):
            if node is None:
                return -1

            return max(recursive(node.left), recursive(node.right)) + 1

        return recursive(self)

    def show(self):
        def recursive(node):
            if node is None:
                return '()'
            else:
                return f'({node.value} {recursive(node.left)} {recursive(node.right)})'

        return recursive(self)

    def change_to_height(self):
        self.value = self.height()
        if self.right is not None:
            self.right.change_to_height()
        if self.left is not None:
            self.left.change_to_height()
        return self


def str_into_list(string):
    string = string.replace('(', '[').replace(')', ']').replace(' ', ',')
    string = ''.join([item if item == '[' or item == ']' or item == ',' else f"'{item}'" for item in string])
    return ast.literal_eval(string)


def recursive_insert(node):
    tree = BinaryTree(node[0])
    if node[1]:
        tree.left = recursive_insert(node[1])
    if node[2]:
        tree.right = recursive_insert(node[2])
    return tree


def balance_tree(node):
    if node is None:
        return None

    if node.left is not None and node.right is not None:
        tree = BinaryTree(node.left.value - node.right.value)
        tree.right = balance_tree(node.right)
        tree.left = balance_tree(node.left)
        return tree

    if node.left is not None:
        tree = BinaryTree(node.left.value + 1)
        tree.left = balance_tree(node.left)
        return tree

    if node.right is not None:
        tree = BinaryTree(-node.right.value - 1)
        tree.right = balance_tree(node.right)
        return tree

    return BinaryTree(0)


raw = input()
lst = str_into_list(raw)
tree = recursive_insert(lst)
tree.change_to_height()
tree = balance_tree(tree)
print(tree.show())
