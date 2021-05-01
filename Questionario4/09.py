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


def str_into_tree(string):

