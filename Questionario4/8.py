class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

    def insert(self, value):
        if self.value is None:
            self.value = value
            return self

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

    def prefix_show(self):
        lst = [self.value]
        if self.left is not None:
            lst.append(self.left.prefix_show())
        if self.right is not None:
            lst.append(self.right.prefix_show())
        return lst

    def infix_show(self):
        lst = []
        if self.left is not None:
            lst.append(self.left.infix_show())
        lst.append(self.value)
        if self.right is not None:
            lst.append(self.right.infix_show())
        return lst

    def postfix_show(self):
        lst = []
        if self.left is not None:
            lst.append(self.left.postfix_show())
        if self.right is not None:
            lst.append(self.right.postfix_show())
        lst.append(self.value)
        return lst


def print_lst(lst):
    temp = str(lst)
    print(temp.replace('[', '').replace(']', '').replace(',', '').replace('None', ''))


def process_command(tree, command):
    if command == 'in':
        print_lst(tree.infix_show())
        return tree

    if command == 'pre':
        print_lst(tree.prefix_show())
        return tree

    if command == 'pos':
        print_lst(tree.postfix_show())
        return tree

    return tree.insert(int(command))


tree = BinarySearchTree(None)

while True:
    command = input()
    if command == 'quack':
        break

    tree = process_command(tree, command)
