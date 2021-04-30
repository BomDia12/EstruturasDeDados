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

    def height(self):
        def recursive(node):
            if node is None:
                return -1

            return max(recursive(node.left), recursive(node.right)) + 1

        height = recursive(self)
        return height if height > 0 else 0


n = int(input())
nums = [int(item) for item in input().split()]
tree = BinarySearchTree(nums.pop(0))
[tree.insert(num) for num in nums]
print(tree.height())
