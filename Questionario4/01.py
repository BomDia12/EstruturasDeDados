def altura(raiz):

    def recursive(raiz):
        if raiz is None:
            return -1

        return max(recursive(raiz.esq), recursive(raiz.dir)) + 1

    result = recursive(raiz)

    return result if result > 0 else 0
