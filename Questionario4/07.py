class Arvore():
    def __init__(self, dado):
        self.dado = dado
        self.filhos = []


def leia():
    def recursive_input():
        brute = input().split()
        processed = [[int(brute[i]), int(brute[i + 1])] for i in range(0, len(brute), 2)]
        return [[node[0], recursive_input()] if node[1] > 0 else [node[0], None] for node in processed]

    def recursive_insert(node):
        if node[1] is None:
            return Arvore(node[0])

        tree = Arvore(node[0])
        for child in node[1]:
            tree.filhos.append(recursive_insert(child))
        return tree

    data = recursive_input()
    return recursive_insert(data[0])
