def mostra(tree, div):

    def recursive(inner_tree, inner_div):
        for leaf in inner_tree.filhos:
            print(inner_div + str(leaf.dado))
            recursive(leaf, inner_div + div)

    print(tree.dado)
    recursive(tree, div)
