def mostra(raiz):

    def recursive(raiz):
        if raiz is None:
            return '()'
        else:
            return f'({raiz.dado} {recursive(raiz.esq)} {recursive(raiz.dir)})'

    str = recursive(raiz)
    print(str)
