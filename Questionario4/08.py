class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

    def insert(self, value):
        if value > self.value and self.right is None:
            self.right = BinarySearchTree(value)
            return self

        if value > self.value:
            self.right.insert(value)
            return self

        if self.left is None:
            self.left = BinarySearchTree(value)
            return self

        self.left.insert(value)
        return self
